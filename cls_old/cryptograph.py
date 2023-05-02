from cryptography.fernet import Fernet

fernet = Fernet(Fernet.generate_key())

class Cryptograph:
    def get_encrypt(self, message):
        return fernet.encrypt(message.encode())

    def get_decrypt(self, message):
        return fernet.decrypt(message).decode()