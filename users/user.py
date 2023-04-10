import hashlib
import secrets

class User:
    def __init__(self, username, password, salt = None):
        self.username = username
        if salt:
            self.salt = salt
            self.password_hash = password
        else:
            self.salt = secrets.token_hex(16)
            self.password_hash = hashlib.sha256(password.encode('utf-8') + str(self.salt).encode('utf-8')).hexdigest()

    def check_password(self, password):
        password_hash = hashlib.sha256(password.encode('utf-8') + self.salt).hexdigest()
        return password_hash == self.password_hash
