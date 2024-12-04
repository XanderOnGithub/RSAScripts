# RSA Encryption and Decryption

This repository contains two Python scripts for performing RSA encryption and decryption using a private and public keys for encryption.

## Overview

- `Encrypt.py`: Encrypts a message using a private RSA key.
- `Decrypt.py`: Decrypts a message using a public RSA key.

These scripts demonstrate basic asymmetric encryption and decryption techniques using RSA, where:

- The private key is used to encrypt the data (instead of the usual public key encryption).
- The public key is used to decrypt the data.

### Warning:
This is a non-standard approach to RSA encryption. Typically, the **public key** is used for encryption,n and the **private key** is used for decryption. However, for this example, the reverse is implemented.

## Requirements

- Python 3.x


