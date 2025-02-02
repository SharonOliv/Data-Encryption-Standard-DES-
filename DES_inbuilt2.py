from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_file(input_file, output_file, key, iv):
    cipher=DES3.new(key,DES3.MODE_CBC,iv)
    with open(input_file,'rb') as f:
        plaintext=f.read()

    padded_text=pad(plaintext,DES3.block_size)
    ciphertext=cipher.encrypt(padded_text)
    with open(output_file,'wb') as f:
        f.write(iv+ciphertext)

    print(f"File '{input_file}' encrypted and saved as '{output_file}'\n")

def decrypt_file(input_file,output_file,key):
    with open(input_file,'rb') as f:
        iv=f.read(8)
        ciphertext=f.read()

    decipher=DES3.new(key,DES3.MODE_CBC,iv)
    decrypted_padded_text=decipher.decrypt(ciphertext)
    try:
        decrypted_text=unpad(decrypted_padded_text, DES3.block_size)
        with open(output_file,'wb') as f:
            f.write(decrypted_text)
        print(f"File '{input_file}' is decrypted and saved as '{output_file}'\n")
    except ValueError:
        print("Decryption failed!!")

#Get key
key=get_random_bytes(24)
iv=get_random_bytes(8)

encrypt_filename=input("Enter the file name to encrypt: ")
encrypted_filename=input("Enter the output encrypted file name: ")
encrypt_file(encrypt_filename,encrypted_filename,key,iv)

decrypt_filename=input("Enter the file name to decrypt: ")
decrypted_filename=input("Enter the file name to save decrypted content: ")
decrypt_file(decrypt_filename,decrypted_filename,key)
