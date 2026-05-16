from art import logo

print(logo)
alphabets='abcdefghijklmnopqrstuvwxyz'

direction=input("Enter the 'encode' for encoding and 'decode' for decoding: ")
if direction != "encode" and direction != "decode":
    print("Run again program and Please type 'encode' or 'decode' for encryption or 'decode' for decryption\n")
else:
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
if direction=="encode":
    def encrypt(original_text, shift_amount):
        cipher_text = ""
        for letter in original_text:
            shifted_position=alphabets.index(letter)+shift_amount #7->9
            shifted_position=shifted_position%len(alphabets)
            cipher_text=cipher_text+alphabets[shifted_position]
        print("Here is the encrypted message:",cipher_text)
    encrypt(original_text=text,shift_amount=shift)
elif direction=="decode":
    def decrypt(original_text,shifted_amount):
        cipher_text = ""
        for letter in original_text:
            shifted_position=alphabets.index(letter)-shifted_amount
            shifted_position=shifted_position%len(alphabets)
            cipher_text=cipher_text+alphabets[shifted_position]
        print("Here is the decrypted message:",cipher_text)
    decrypt(text,shift)