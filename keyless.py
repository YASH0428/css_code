def keyless_transposition_encrypt(plain_text):
    cipher_text = ""
    for i in range(2):  # Number of rows in the transposition grid
        j = i
        while j < len(plain_text):
            cipher_text += plain_text[j]
            j += 2
    return cipher_text

def keyless_transposition_decrypt(cipher_text):
    plain_text = ""
    grid_size = (len(cipher_text) + 1) // 2  # Calculate the number of rows in the transposition grid
    row1 = cipher_text[:grid_size]
    row2 = cipher_text[grid_size:]
    for i in range(grid_size):
        if i < len(row1):
            plain_text += row1[i]
        if i < len(row2):
            plain_text += row2[i]
    return plain_text

# Example usage
message = "Hello, World!"

encrypted_message = keyless_transposition_encrypt(message)
print("Encrypted message:", encrypted_message)

decrypted_message = keyless_transposition_decrypt(encrypted_message)
print("Decrypted message:", decrypted_message)
