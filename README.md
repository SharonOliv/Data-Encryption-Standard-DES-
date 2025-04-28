# Data Encryption Standard (Triple DES)
This repository contains an implementation that explains how to **encrypt** and **decrypt** data using **Triple DES (DES3)** encryption.

## Overview

This repo demonstrates:
- The working of **Triple DES (DES3)** encryption and decryption algorithms.
- How plaintext is securely encrypted into ciphertext.
- How the encrypted ciphertext is decrypted back into the original plaintext.

**Triple DES (DES3)** applies the DES encryption algorithm three times to each data block, providing greater security compared to the original DES.

## Features

- Encrypt text data using Triple DES.
- Decrypt encrypted data back to its original form.
- Use of secure symmetric encryption techniques.
- Clear and simple example of Triple DES usage in Python.

## Technologies Used

- Python 3
- `pycryptodome` library (`Crypto.Cipher.DES3`)

## How to Run

1. Install dependencies:
   ```bash
   pip install pycryptodome
   ```

2. Run the script:
   ```bash
   python DES_inbuilt1.py
   ```
   give text as input to encrypt or decrypt data

3. Run the script:
   ```bash
   python DES_inbuilt2.py
   ```
   give text file as input to encrypt or decrypt data
   
4. The script will demonstrate encryption of a sample message and its decryption.

## Notes

- Triple DES is more secure than the original DES but is slower than newer standards like AES.
- Triple DES is still used in legacy applications but is being phased out in favor of stronger encryption methods.
- This project is intended for educational purposes and should not be used for securing sensitive information in production.
