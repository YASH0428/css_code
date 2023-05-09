def transposition_encrypt(plain_text, key):
    cipher_text = ""
    num_columns = len(key)
    num_rows = (len(plain_text) + num_columns - 1) // num_columns
    grid = [[''] * num_columns for _ in range(num_rows)]
    index = 0

    for col in range(num_columns):
        col_index = key[col]
        row_index = 0

        while row_index < num_rows and index < len(plain_text):
            grid[row_index][col_index] = plain_text[index]
            row_index += 1
            index += 1

    for row in grid:
        cipher_text += ''.join(row)

    return cipher_text

def transposition_decrypt(cipher_text, key):
    plain_text = ""
    num_columns = len(key)
    num_rows = (len(cipher_text) + num_columns - 1) // num_columns
    grid = [[''] * num_columns for _ in range(num_rows)]
    index = 0

    for col in key:
        col_index = col
        row_index = 0

        while row_index < num_rows and index < len(cipher_text):
            grid[row_index][col_index] = '*'
            row_index += 1
            index += 1

    index = 0

    for col in range(num_columns):
        col_index = key[col]
        row_index = 0

        while row_index < num_rows:
            if grid[row_index][col_index] == '*':
                grid[row_index][col_index] = cipher_text[index]
                index += 1
            row_index += 1

    for row in grid:
        plain_text += ''.join(row)

    return plain_text

# Take input from the user
message = input("Enter the message: ")
key = input("Enter the encryption key (comma-separated values): ")
encryption_key = [int(k.strip()) for k in key.split(",")]

encrypted_message = transposition_encrypt(message, encryption_key)
print("Encrypted message:", encrypted_message)

decrypted_message = transposition_decrypt(encrypted_message, encryption_key)
print("Decrypted message:", decrypted_message)
