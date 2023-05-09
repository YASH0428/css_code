def custom_hash(input_string):
    hash_value = 0

    # Concatenate the ASCII values of each character
    for char in input_string:
        hash_value += ord(char)

    # Perform character rotation
    rotated_hash = 0
    for i in range(len(input_string)):
        rotated_hash += (hash_value << i) | (hash_value >> (len(input_string) - i))

    # Apply modulo arithmetic
    hash_value = rotated_hash % 1000  # Modulo 1000 to limit the hash value to a three-digit number

    return hash_value

# Example usage
message = input("Enter a message: ")
hashed_value = custom_hash(message)
print("Hashed value:", hashed_value)
