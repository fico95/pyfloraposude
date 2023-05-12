import hashlib
import secrets
import re

class User:
    def __init__(self, username, password, salt = None):
        self.username = username
        if salt:
            self.salt = salt
            self.passwordHash = password
        else:
            self.salt = None
            self.setPassword(password)

    def setPassword(self, password):
        if (not self.salt):
            self.salt = secrets.token_hex(16)
        self.passwordHash = hashlib.sha256(password.encode('utf-8') + str(self.salt).encode('utf-8')).hexdigest()

    def checkPassword(self, password):
        passwordHash = hashlib.sha256(password.encode('utf-8') + str(self.salt).encode('utf-8')).hexdigest()
        return passwordHash == self.passwordHash
    
    @staticmethod
    def checkStrongPassword(password: str) -> bool:
        strongPasswordRegex =  "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
        return re.search(strongPasswordRegex, password) != None