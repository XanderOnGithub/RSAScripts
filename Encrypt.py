# Private key values
n = 0  # Modulus
d = 0 # Private exponent

# Function to encrypt a message using the private key
def encrypt_with_private_key(message, n, d):
    # Convert the message to ASCII values
    ascii_values = [ord(char) for char in message]
    
    # Encrypt each ASCII value using the RSA formula: C = M^d mod n
    ciphertext = [pow(m, d, n) for m in ascii_values]
    return ciphertext

# Message to encrypt
message = ""

# Encrypt the message with the private key
ciphertext = encrypt_with_private_key(message, n, d)

# Print the ciphertext
print(f"Ciphertext (signed): {ciphertext}")
