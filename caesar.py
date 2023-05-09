def caesar_encrypt(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                cipher_text += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                cipher_text += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def caesar_decrypt(cipher_text, shift):
    plain_text = ""
    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                plain_text += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                plain_text += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            plain_text += char
    return plain_text

# Input from the user
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))

encrypted_message = caesar_encrypt(message, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = caesar_decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)
