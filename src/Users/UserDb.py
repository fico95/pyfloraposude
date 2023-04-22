import sqlite3

from Users.User import User

class UserDb:
    def __init__(self, dbPath):
        self.dbPath = dbPath
        self.conn = sqlite3.connect(self.dbPath)
        self.createTable()

    def createTable(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS users
                            (id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            salt TEXT NOT NULL,
                            passwordHash TEXT NOT NULL)''')
        self.conn.commit()

    def addUser(self, user):
        self.conn.execute('''INSERT INTO users (username, salt, passwordHash)
                            VALUES (?, ?, ?)''', (user.username, user.salt, user.passwordHash))
        self.conn.commit()

    def getUser(self, username):
        cur = self.conn.cursor()

        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cur.fetchone()
        cur.close()
        if row:
            user = User(row[1], row[3], row[2])
            return user
        return None
    
    def updateUserPassword(self, username, newPassword):
        user = self.getUser(username)
        if user:
            user.setPassword(newPassword)
            self.conn.execute("UPDATE users SET salt=?, passwordHash=? WHERE username=?", (user.salt, user.passwordHash, user.username))
            self.conn.commit()
            return True
        return False

    def deleteUser(self, username):
        self.conn.execute("DELETE FROM users WHERE username=?", (username,))
        self.conn.commit()

    def deleteAllUsers(self):
        self.conn.execute("DELETE FROM users")
        self.conn.commit()

    def getNumUsers(self):
        cur = self.conn.cursor()
        cur.execute("SELECT COUNT(*) FROM users")
        numUsers = cur.fetchone()[0]
        cur.close()
        return numUsers

