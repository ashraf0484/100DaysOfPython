import caesar_cipher_extra
import os

os.system("clear")

print(caesar_cipher_extra.logo)
cont = "y"

while cont == "y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))      


    def caesar(plain_text, shift, direction):
        converted_word = ""
        if direction.lower() == "decode":
            shift *= -1
            
        for i in plain_text:
            if i not in caesar_cipher_extra.alphabet:
                converted_word += i
            else : 
                letter_index = caesar_cipher_extra.alphabet.index(i)
                shifted_letter_index = letter_index + shift
                converted_word += caesar_cipher_extra.alphabet[shifted_letter_index%len(caesar_cipher_extra.alphabet)]
        print(f"The {direction.lower()}d text is {converted_word}.")        

    caesar(text, shift, direction)
    cont = input("Press y to continue...")
    os.system("clear")
print("Thank you for using me!")

                # if direction == "encode":
                #     if shifted_letter_index >= len(caesar_cipher_extra.alphabet) :
                #         converted_word += caesar_cipher_extra.alphabet[shifted_letter_index%len(caesar_cipher_extra.alphabet)]
                #     else:    
                #         converted_word += caesar_cipher_extra.alphabet[shifted_letter_index]
                # elif direction == "decode":
                #     if shifted_letter_index <= len(caesar_cipher_extra.alphabet) :
                #         converted_word += caesar_cipher_extra.alphabet[shifted_letter_index]
                #     else:    
                #         converted_word += caesar_cipher_extra.alphabet[shifted_letter_index%len(caesar_cipher_extra.alphabet)]