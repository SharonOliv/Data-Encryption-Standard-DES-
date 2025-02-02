import binascii
from Crypto.Util.Padding import pad, unpad

#Initial permutation Tables
IP=[58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]

#Final permutation table
FP=[40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25]

#Expansion Table
E=[32, 1, 2, 3, 4, 5, 4, 5,
    6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27,
    28, 29, 28, 29, 30, 31, 32, 1]

#Permutation Table
P=[16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25]

#S-box
S_BOX=[[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]]

def permute(block, table):
    permuted_block=[]
    for i in table:
        permuted_block.append(block[i-1]) 
    return permuted_block

def feistel_function(right,key):
    expanded=permute(right,E)
    xored = []
    for i in range(len(expanded)): 
        xored.append(expanded[i]^key[i])  
    return permute(xored,P)

def des_encrypt(plaintext, key):
    plaintext_padded = pad(plaintext.encode(), 8)  # Pad to 8-byte blocks
    plaintext_bits = []
    for bit in bin(int(binascii.hexlify(plaintext_padded), 16))[2:].zfill(64):
        plaintext_bits.append(int(bit))

    key_bits=[]
    for bit in bin(int(binascii.hexlify(key.encode()), 16))[2:].zfill(64):
        key_bits.append(int(bit))

    permuted=permute(plaintext_bits,IP)
    left=permuted[:32]
    right=permuted[32:]
    for round in range(16):
        temp=right
        new_right=[]
        feistel_result=feistel_function(right,key_bits[:48])
        for i in range(len(feistel_result)):
            new_right.append(left[i]^feistel_result[i])

        right=new_right
        left=temp

    final_block=permute(right+left,FP)
    cipher_bits_str=''.join(map(str,final_block))
    cipher_hex=hex(int(cipher_bits_str,2))[2:].zfill(16)
    return cipher_hex


def des_decrypt(ciphertext, key):
    ciphertext_bits=[]
    for bit in bin(int(ciphertext, 16))[2:].zfill(64):
        ciphertext_bits.append(int(bit))

    key_bits = []
    for char in key:
        key_bits.extend([int(bit) for bit in bin(ord(char))[2:].zfill(8)])

    permuted=permute(ciphertext_bits,IP)
    left=permuted[:32]
    right=permuted[32:]
    
    round_key=key_bits[:48]

    for round in range(15,-1,-1): 
        temp=left
        new_left=[]
        feistel_result=feistel_function(left,round_key)
        for i in range(len(feistel_result)):
            new_left.append(right[i]^feistel_result[i])

        left=new_left
        right=temp

    final_block=permute(left + right, FP)
    decrypted_bits_str=''.join(map(str, final_block))
    decrypted_hex=hex(int(decrypted_bits_str, 2))[2:].zfill(16)

    try:
        decrypted_text = binascii.unhexlify(decrypted_hex)
        decrypted_text = unpad(decrypted_text, 8).decode()  # Remove padding
    except (UnicodeDecodeError, ValueError):
        decrypted_text = "[Decryption Error]"

    return decrypted_text



plaintext=input("Enter the text you want to encrypt:\n")
key="12345678"
cipher_text=des_encrypt(plaintext, key)
print(f"Cipher Text: {cipher_text}\n")

ciphertext=input("Enter text to decrypt (in hexadecimal only):\n")
decrypted_text=des_decrypt(ciphertext,key)
print(f"Decrypted Text: {decrypted_text}")
