from cryptography.fernet import Fernet
import base64


def encrypt_the_file(file_path):

    chipher = Fernet(base64.b64encode(b'12345678901234567890123456789012'))

    with open(file_path, 'rb') as file:
        e_file = file.read()

    encrypted_file = chipher.encrypt(e_file)

    with open(file_path+'.enc', 'wb') as file:
        file.write(encrypted_file)
