#program a public and private key

from os import chmod
from Crypto.PublicKey import RSA

key = RSA.generate(2048) #gerar chaves

private_key = key.export_key() #exportar chave privada




print("Key Generated with success")