# Given
n = 512153
e = 271
ciphertext = [436331, 132442, 124426, 124426, 51005, 68886, 74732, 206298, 124426, 29706, 398694,
398694, 101277]

# Decrypt each ciphertext value using the public key
decrypted = [pow(c, e, n) for c in ciphertext]

# Function to split a number into 2-digit ASCII chunks
def split_into_ascii(num):
    num_str = str(num)
    return [int(num_str[i:i+2]) for i in range(0, len(num_str), 2)]

# Split decrypted numbers into ASCII chunks and decode
plaintext = []
for num in decrypted:
    chunks = split_into_ascii(num)
    plaintext.extend(chunks)

# Convert to ASCII characters
decoded_message = ''.join(chr(chunk) for chunk in plaintext)
print(f"Decrypted message: {decoded_message}")
