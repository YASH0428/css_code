import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y


def generate_prime_number(bits):
    while True:
        num = random.getrandbits(bits)
        if num % 2 != 0 and is_prime(num):
            return num


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_keypair(p, q):
    # Step 1: Compute n
    n = p * q

    # Step 2: Compute totient (phi) of n
    phi = (p - 1) * (q - 1)

    # Step 3: Find e (public key)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Step 4: Find d (private key)
    _, d, _ = extended_gcd(e, phi)
    d = d % phi
    if d < 0:
        d += phi

    # Return public and private keys
    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher


def decrypt(cipher, private_key):
    d, n = private_key
    message = [chr(pow(char, d, n)) for char in cipher]
    return ''.join(message)


# Example usage
p = generate_prime_number(128)
q = generate_prime_number(128)
public_key, private_key = generate_keypair(p, q)

message = "Hello, RSA!"
print("Original message:", message)

encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)
