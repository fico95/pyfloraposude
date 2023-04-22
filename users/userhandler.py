from PySide2.QtCore import QObject, Signal, Slot, Property
from users.user import User
from users.userdatabase import UserDatabase

class UserHandler(QObject):
    num_users_changed = Signal()

    @Property(int, notify=num_users_changed)
    def num_users(self):
        return self.user_db.get_num_users()
    

    def __init__(self, db_path, parent=None):
        super().__init__(parent)
        self.user_db = UserDatabase(db_path)

        num_users = self.num_users
        if num_users > 1:
            print(f"Deleting {num_users} users...")
            self.user_db.delete_all_users()

    @Slot(str, str, result=bool)
    def add_user(self, username, password):
        try:
            user = User(username, password)
            self.user_db.add_user(user)
            self.num_users_changed.emit()
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
            self.num_users_changed.emit()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        
    @Slot(result=bool)
    def delete_all_users(self):
        try:
            self.user_db.delete_all_users()
            self.num_users_changed.emit()
            return True
        except Exception as e:
            print(f"Error deleting all users: {e}")
            return False
        
    @Slot(result=bool)
    def user_exists(self):
        return self.num_user > 0
