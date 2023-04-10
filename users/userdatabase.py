import sqlite3
import users.user as User

class UserDatabase:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS users
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              username TEXT UNIQUE NOT NULL,
                              salt TEXT NOT NULL,
                              password_hash TEXT NOT NULL)''')
        self.conn.commit()

    def add_user(self, user):
        self.conn.execute('''INSERT INTO users (username, salt, password_hash)
                             VALUES (?, ?, ?)''', (user.username, user.salt, user.password_hash))
        self.conn.commit()

    def get_user(self, username):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cur.fetchone()
        cur.close()
        if row:
            user = User(row[1], row[3], row[2])
            return user
        return None

    def delete_user(self, username):
        self.conn.execute("DELETE FROM users WHERE username=?", (username,))
        self.conn.commit()
