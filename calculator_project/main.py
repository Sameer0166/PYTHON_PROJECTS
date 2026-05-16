from cal_art import logo
print(logo)
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return f"{a}/0 is undefined"
    else:
        return a/b
def power(a,b):
    return a**b
def mod(a,b):
    return a%b

operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "**":power,
    "%":mod,
}
def calculator():
    print(logo)
    should_accumulate=True
    a = float(input("Enter the first number: "))
    while should_accumulate:
        for symbol in operation:
            print(symbol)
        operation_symbol=input("Enter the operator:")
        b=float(input("Enter the second number: "))
        answer=operation[operation_symbol](a,b)
        print(f"The result of({a}{operation_symbol}{b})=", answer)


        choice=input(f"Type 'y' continue calculating with the previous ({answer})or type 'n' to exit or type 'new' to start new calculator:")
        if choice=='y':
            a=answer
        elif choice=='new':
            should_accumulate=False
            print("\n"*20)
            calculator()
        else:
            print("Exited from the calculator")
            exit()
calculator()