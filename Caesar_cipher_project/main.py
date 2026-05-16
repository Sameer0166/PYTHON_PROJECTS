from debugpy.launcher import output

alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
from art import logo
print(logo)

def caesar_cipher(original_text, shift_amount,encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:

        if letter not in alphabets:
            output_text+=letter
        else:


            shifted_position=alphabets.index(letter)+shift_amount
            shifted_position=shifted_position%len(alphabets)
            output_text+=alphabets[shifted_position]
    print(f"Here is the {encode_or_decode}d message:",output_text)
should_continue = True

while should_continue:

    direction = input("Type 'encode' for encryption or 'decode' for decryption:\n")
    if direction!="encode" and direction!="decode":
        print("Please type 'encode' or 'decode' for encryption or 'decode' for decryption\n")
        should_continue = True
    if direction=="encode" or direction=="decode":
        text = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        caesar_cipher(original_text=text,shift_amount=shift,encode_or_decode=direction)
        restart=input("type 'yes' to continue again otherwise 'no':\n")
        if restart =="no":
            should_continue = False
            print("goodbye")
