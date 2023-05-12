import sqlite3

from Users.User import User

class UserDb:
    def __init__(self, dbPath):
        self.dbPath = dbPath
        self.conn = sqlite3.connect(self.dbPath)
        self.enableForeignKeys()
        self.createTable()

    def __del__(self):
        self.conn.close()

    def enableForeignKeys(self):
        cursor = self.conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        self.conn.commit()

    def createTable(self):
        self.conn.execute("""CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            salt TEXT NOT NULL,
                            passwordHash TEXT NOT NULL)""")
        self.conn.commit()

    def addUser(self, user: User):
        self.conn.execute("""INSERT INTO users (username, salt, passwordHash)
                            VALUES (?, ?, ?)""", (user.username, user.salt, user.passwordHash))
        self.conn.commit()

    def fetchUserByUsername(self, username: str) -> User:
        cursor = self.conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        if row is None:
            return None
        id, username, salt, passwordHash = row
        user = User(username, passwordHash, salt)
        return user
    
    def updateUserPassword(self, username: str, newPassword: str) -> bool:
        user = self.fetchUserByUsername(username)
        if user:
            user.setPassword(newPassword)
            self.conn.execute("UPDATE users SET salt=?, passwordHash=? WHERE username=?", (user.salt, user.passwordHash, user.username))
            self.conn.commit()
            return True
        return False

    def removeUserByUsername(self, username: str):
        self.conn.execute("DELETE FROM users WHERE username=?", (username,))
        self.conn.commit()

    def removeUsers(self):
        self.conn.execute("DELETE FROM users")
        self.conn.commit()

    def usersCount(self) -> int:
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        usersCount = cursor.fetchone()[0]
        return usersCount

