import math
import sys
import re
from decimal import Decimal, InvalidOperation, getcontext
from typing import List, Optional, Callable, Dict, Any
from dataclasses import dataclass

try:
    from cal_art import logo
except ImportError:
    logo = "Calculator"

# Increase precision for decimals
getcontext().prec = 28

# --- Tokenizer ---

class TokenType:
    NUMBER = "NUMBER"
    PLUS = "PLUS"
    MINUS = "MINUS"
    MUL = "MUL"
    DIV = "DIV"
    MOD = "MOD"
    POW = "POW"
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    IDENT = "IDENT"
    EOF = "EOF"

@dataclass
class Token:
    type: str
    value: Any
    pos: int

class LexerError(Exception):
    def __init__(self, msg: str, pos: int):
        self.msg = msg
        self.pos = pos
        super().__init__(self.msg)

class ParseError(Exception):
    def __init__(self, msg: str, pos: int):
        self.msg = msg
        self.pos = pos
        super().__init__(self.msg)

class EvalError(Exception): pass

def tokenize(text: str) -> List[Token]:
    tokens = []
    # Updated NUMBER regex to match .5, 5., 0.5, 5
    token_specification = [
        ('NUMBER',   r'(?:\d+\.\d*|\.\d+|\d+)'),
        ('IDENT',    r'[a-zA-Z_]+'),
        ('PLUS',     r'\+'),
        ('MINUS',    r'-'),
        ('POW',      r'\^|\*\*'),
        ('MUL',      r'\*'),
        ('DIV',      r'/'),
        ('MOD',      r'%'),
        ('LPAREN',   r'\('),
        ('RPAREN',   r'\)'),
        ('SKIP',     r'[ \t\n]+'),
        ('MISMATCH', r'.'),
    ]
    
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    
    for mo in re.finditer(tok_regex, text):
        kind = mo.lastgroup
        value = mo.group()
        pos = mo.start()
        
        if kind == 'NUMBER':
            tokens.append(Token(TokenType.NUMBER, Decimal(value), pos))
        elif kind == 'IDENT':
            tokens.append(Token(TokenType.IDENT, value, pos))
        elif kind == 'PLUS': tokens.append(Token(TokenType.PLUS, value, pos))
        elif kind == 'MINUS': tokens.append(Token(TokenType.MINUS, value, pos))
        elif kind == 'POW': tokens.append(Token(TokenType.POW, value, pos))
        elif kind == 'MUL': tokens.append(Token(TokenType.MUL, value, pos))
        elif kind == 'DIV': tokens.append(Token(TokenType.DIV, value, pos))
        elif kind == 'MOD': tokens.append(Token(TokenType.MOD, value, pos))
        elif kind == 'LPAREN': tokens.append(Token(TokenType.LPAREN, value, pos))
        elif kind == 'RPAREN': tokens.append(Token(TokenType.RPAREN, value, pos))
        elif kind == 'SKIP': continue
        elif kind == 'MISMATCH':
            raise LexerError(f"Unexpected character {value!r}", pos)
            
    tokens.append(Token(TokenType.EOF, None, len(text)))
    return tokens

# --- AST Nodes ---

class AST: pass

@dataclass
class BinOp(AST):
    left: AST
    op: Token
    right: AST

@dataclass
class UnaryOp(AST):
    op: Token
    expr: AST

@dataclass
class Num(AST):
    token: Token
    value: Decimal

@dataclass
class FuncCall(AST):
    func_name: str
    arg: AST
    pos: int

@dataclass
class Constant(AST):
    name: str
    pos: int

# --- Parser (Recursive Descent) ---

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def error(self, msg: str):
        raise ParseError(msg, self.current_token.pos)

    def eat(self, token_type: str):
        if self.current_token.type == token_type:
            self.pos += 1
            if self.pos < len(self.tokens):
                self.current_token = self.tokens[self.pos]
        else:
            self.error(f"Expected {token_type}, got {self.current_token.type}")

    def factor(self) -> AST:
        """factor : (PLUS | MINUS) factor | NUMBER | LPAREN expr RPAREN | IDENT LPAREN expr RPAREN | IDENT"""
        token = self.current_token

        if token.type == TokenType.PLUS:
            self.eat(TokenType.PLUS)
            return UnaryOp(op=token, expr=self.factor())
        elif token.type == TokenType.MINUS:
            self.eat(TokenType.MINUS)
            return UnaryOp(op=token, expr=self.factor())
        elif token.type == TokenType.NUMBER:
            self.eat(TokenType.NUMBER)
            return Num(token=token, value=token.value)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node
        elif token.type == TokenType.IDENT:
            ident_token = token
            self.eat(TokenType.IDENT)
            
            if self.current_token.type == TokenType.LPAREN:
                # Function call
                self.eat(TokenType.LPAREN)
                arg_node = self.expr()
                self.eat(TokenType.RPAREN)
                return FuncCall(func_name=ident_token.value, arg=arg_node, pos=ident_token.pos)
            else:
                # Constant
                return Constant(name=ident_token.value, pos=ident_token.pos)
            
        self.error(f"Unexpected token in factor: {token.value}")

    def power(self) -> AST:
        """power : factor (POW power)?"""
        node = self.factor()

        if self.current_token.type == TokenType.POW:
            token = self.current_token
            self.eat(TokenType.POW)
            node = BinOp(left=node, op=token, right=self.power())

        return node

    def term(self) -> AST:
        """term : power ((MUL | DIV | MOD) power | implicit_mul)*"""
        node = self.power()

        while True:
            if self.current_token.type in (TokenType.MUL, TokenType.DIV, TokenType.MOD):
                token = self.current_token
                self.eat(token.type)
                node = BinOp(left=node, op=token, right=self.power())
            elif self.current_token.type in (TokenType.LPAREN, TokenType.IDENT):
                # Implicit multiplication: e.g. 2(3) or 2sin(90) or 2pi
                virtual_token = Token(TokenType.MUL, '*', self.current_token.pos)
                node = BinOp(left=node, op=virtual_token, right=self.power())
            else:
                break

        return node

    def expr(self) -> AST:
        """expr : term ((PLUS | MINUS) term)*"""
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            self.eat(token.type)
            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self) -> AST:
        node = self.expr()
        if self.current_token.type != TokenType.EOF:
            self.error("Unexpected token after valid expression")
        return node

# --- Evaluator ---

def _div(a: Decimal, b: Decimal) -> Decimal:
    if b == Decimal('0'): raise ZeroDivisionError("Division by zero")
    return a / b

def _mod(a: Decimal, b: Decimal) -> Decimal:
    if b == Decimal('0'): raise ZeroDivisionError("Modulo by zero")
    return a % b

def _sqrt(a: Decimal) -> Decimal:
    if a < Decimal('0'): raise ValueError("Square root of negative number")
    return a.sqrt()

def _sin(a: Decimal) -> Decimal:
    return Decimal(str(math.sin(math.radians(float(a)))))

def _cos(a: Decimal) -> Decimal:
    return Decimal(str(math.cos(math.radians(float(a)))))

def _tan(a: Decimal) -> Decimal:
    return Decimal(str(math.tan(math.radians(float(a)))))

def _log10(a: Decimal) -> Decimal:
    if a <= Decimal('0'): raise ValueError("Logarithm of non-positive number")
    return a.log10()

def _ln(a: Decimal) -> Decimal:
    if a <= Decimal('0'): raise ValueError("Natural logarithm of non-positive number")
    return a.ln()

def _fact(a: Decimal) -> Decimal:
    if a < Decimal('0') or a % Decimal('1') != Decimal('0'):
        raise ValueError("Factorial requires non-negative integer")
    return Decimal(str(math.factorial(int(a))))

FUNCTIONS: Dict[str, Callable[[Decimal], Decimal]] = {
    "sqrt": _sqrt,
    "sin": _sin,
    "cos": _cos,
    "tan": _tan,
    "log": _log10,
    "ln": _ln,
    "fact": _fact
}

CONSTANTS: Dict[str, Decimal] = {
    "pi": Decimal(str(math.pi)),
    "e": Decimal(str(math.e)),
    "tau": Decimal(str(math.tau))
}

class Evaluator:
    def visit(self, node: AST) -> Decimal:
        method_name = f'visit_{type(node).__name__}'
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node: AST):
        raise EvalError(f"No visit_{type(node).__name__} method")

    def visit_Num(self, node: Num) -> Decimal:
        return node.value

    def visit_Constant(self, node: Constant) -> Decimal:
        name = node.name.lower()
        if name not in CONSTANTS:
            raise EvalError(f"Unknown constant: {name}")
        return CONSTANTS[name]

    def visit_BinOp(self, node: BinOp) -> Decimal:
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_type = node.op.type

        if op_type == TokenType.PLUS: return left + right
        elif op_type == TokenType.MINUS: return left - right
        elif op_type == TokenType.MUL: return left * right
        elif op_type == TokenType.DIV: return _div(left, right)
        elif op_type == TokenType.MOD: return _mod(left, right)
        elif op_type == TokenType.POW:
            if right > Decimal('10000') or right < Decimal('-10000'):
                raise EvalError("Exponent too large")
            try:
                return left ** right
            except InvalidOperation:
                raise EvalError("Invalid exponentiation")
        else:
            raise EvalError(f"Unknown BinOp: {op_type}")

    def visit_UnaryOp(self, node: UnaryOp) -> Decimal:
        expr = self.visit(node.expr)
        if node.op.type == TokenType.PLUS:
            return +expr
        elif node.op.type == TokenType.MINUS:
            return -expr
        else:
            raise EvalError(f"Unknown UnaryOp: {node.op.type}")

    def visit_FuncCall(self, node: FuncCall) -> Decimal:
        arg = self.visit(node.arg)
        func_name = node.func_name.lower()
        if func_name not in FUNCTIONS:
            raise EvalError(f"Unknown function: {func_name}")
        return FUNCTIONS[func_name](arg)

# --- Engine ---

class CalculatorEngine:
    def evaluate(self, expression: str) -> Decimal:
        tokens = tokenize(expression)
        parser = Parser(tokens)
        tree = parser.parse()
        evaluator = Evaluator()
        return evaluator.visit(tree)

# --- CLI Interface ---

def display_error(expr_str: str, pos: int, msg: str):
    print(expr_str)
    print(" " * pos + "^")
    print(f"Error: {msg}")

def print_help():
    print("\n--- Available Operations ---")
    print("Operators: +, -, *, /, %, ^ or **")
    print("Functions: sqrt(), sin(), cos(), tan(), log(), ln(), fact()")
    print("Constants: pi, e, tau")
    print("Commands: clear, history, quit")
    print("Examples:")
    print("  .5 + .5")
    print("  2pi + 2(3+4)")
    print("  sin(pi/2)")
    print("----------------------------\n")

def run_cli():
    print(logo)
    print_help()

    engine = CalculatorEngine()
    previous_result: Optional[Decimal] = None
    history = []
    exit_commands = {'quit', 'stop', 'exit', 'no'}

    while True:
        try:
            if previous_result is not None:
                display_val = previous_result.to_integral() if previous_result % Decimal('1') == Decimal('0') else previous_result
                user_input = input(f"Continue with {display_val}? (Enter expression like '+ 5' or 'clear'/'history'/'quit'): ").strip()
                
                if not user_input:
                    continue
                if user_input.lower() in exit_commands:
                    print("Goodbye!")
                    break
                if user_input.lower() == 'clear':
                    previous_result = None
                    continue
                if user_input.lower() == 'history':
                    print("\n--- Calculation History ---")
                    if not history:
                        print("No history yet.")
                    else:
                        for idx, (expr, res) in enumerate(history, 1):
                            print(f"{idx}. {expr} = {res}")
                    print("---------------------------\n")
                    continue
                
                if re.match(r'^[\+\-\*\/\%\^]', user_input):
                    full_expr = f"{previous_result} {user_input}"
                else:
                    full_expr = user_input

                result = engine.evaluate(full_expr)
                previous_result = result
            else:
                user_input = input("Enter expression (e.g. 2(3+4) or pi/2) or 'history'/'quit': ").strip()
                
                if not user_input:
                    continue
                if user_input.lower() in exit_commands:
                    print("Goodbye!")
                    break
                if user_input.lower() == 'history':
                    print("\n--- Calculation History ---")
                    if not history:
                        print("No history yet.")
                    else:
                        for idx, (expr, res) in enumerate(history, 1):
                            print(f"{idx}. {expr} = {res}")
                    print("---------------------------\n")
                    continue
                    
                full_expr = user_input
                result = engine.evaluate(full_expr)
                previous_result = result

            if previous_result is not None:
                display_val = previous_result.to_integral() if previous_result % Decimal('1') == Decimal('0') else previous_result
                history.append((full_expr, display_val))
                print(f"Result: {display_val}")

        except LexerError as e:
            display_error(full_expr, e.pos, f"Lexer Error: {e.msg}")
            previous_result = None
        except ParseError as e:
            display_error(full_expr, e.pos, f"Syntax Error: {e.msg}")
            previous_result = None
        except ZeroDivisionError as e:
            print(f"Math Error: {e}")
            previous_result = None
        except ValueError as e:
            print(f"Value Error: {e}")
            previous_result = None
        except EvalError as e:
            print(f"Evaluation Error: {e}")
            previous_result = None

if __name__ == "__main__":
    try:
        run_cli()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting...")
        sys.exit(0)
