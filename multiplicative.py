def multiplicative_encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.isupper():
                cipher_text += chr(((ord(char) - 65) * key) % 26 + 65)
            else:
                cipher_text += chr(((ord(char) - 97) * key) % 26 + 97)
        else:
            cipher_text += char
    return cipher_text

def multiplicative_decrypt(cipher_text, key):
    plain_text = ""
    mod_inverse = 0
    for i in range(26):
        if (key * i) % 26 == 1:
            mod_inverse = i
            break
    for char in cipher_text:
        if char.isalpha():
            if char.isupper():
                plain_text += chr(((ord(char) - 65) * mod_inverse) % 26 + 65)
            else:
                plain_text += chr(((ord(char) - 97) * mod_inverse) % 26 + 97)
        else:
            plain_text += char
    return plain_text

# Example usage
message = "Hello, World!"
key = 5

encrypted_message = multiplicative_encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = multiplicative_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
