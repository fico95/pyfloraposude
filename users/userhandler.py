from PySide2.QtCore import QObject, Signal, Slot
from users.user import User
from users.userdatabase import UserDatabase

class UserHandler(QObject):
    def __init__(self, db_path, parent=None):
        super().__init__(parent)
        self.user_db = UserDatabase(db_path)

        num_users = self.user_db.get_num_users()
        if num_users > 1:
            print(f"Deleting {num_users} users...")
            self.user_db.delete_all_users()

    @Slot(str, str, result=bool)
    def add_user(self, username, password):
        try:
            user = User(username, password)
            self.user_db.add_user(user)
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False

    @Slot(str, str, result=bool)
    def authenticate_user(self, username, password):
        try:
            user = self.user_db.get_user(username)
            if not user:
                return False
            return user.check_password(password)
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return False

    @Slot(str, result=bool)
    def delete_user(self, username):
        try:
            self.user_db.delete_user(username)
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        
    @Slot(result=bool)
    def user_exists(self):
        return self.user_db.get_num_users() > 0
