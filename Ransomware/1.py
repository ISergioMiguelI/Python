from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

# Geração de chaves
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Criptografia de um arquivo
def encrypt_file(file_name, public_key):
    # Ler o arquivo
    with open(file_name, 'rb') as f:
        file_data = f.read()

    # Criptografar o arquivo
    public_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    enc_file_data = cipher_rsa.encrypt(file_data)

    # Escrever o arquivo criptografado
    with open(file_name + ".enc", 'wb') as f:
        f.write(enc_file_data)


encrypt_file('C:/Windows/System32/test.txt', public_key)
