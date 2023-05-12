from PySide2.QtCore import QObject, Signal, Slot, Property

from Users.User import User
from Users.UserDb import UserDb

class UserHandler(QObject):
    usersCountChanged = Signal()

    @Property(int, notify=usersCountChanged)
    def usersCount(self):
        return self.userDb.usersCount()

    def __init__(self, dbPath, parent=None):
        super().__init__(parent)
        self.userDb = UserDb(dbPath)

        usersCount = self.usersCount
        if usersCount > 1:
            print(f"Deleting {usersCount} users...")
            self.userDb.removeUsers()

    @Slot(str, result=bool)
    def checkPasswordStrength(self, password: str) -> bool:
        return User.checkStrongPassword(password)
    
    @Slot(str, str, result=bool)
    def addUser(self, username: str, password: str) -> bool:
        if (not self.checkPasswordStrength(password)):
            print("Error adding user: Password is not strong enough.")
            return False
        try:
            user = User(username, password)
            self.userDb.addUser(user)
            self.usersCountChanged.emit()
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False
        return False
        
    @Slot(str, str, str, result=bool)
    def updateUserPassword(self, username: str, oldPassword: str, newPassword: str) -> bool:
        if (not self.checkPasswordStrength(newPassword)):
            print("Error updating user password: New password is not strong enough.")
            return False
        if (not self.authenticateUser(username, oldPassword)):
            print("Error updating user password: Incorrect password or username.")
            return False
        try:
            self.userDb.updateUserPassword(username, newPassword)
            return True
        except Exception as e:
            print(f"Error updating user password: {e}")
            return False

    @Slot(str, str, result=bool)
    def authenticateUser(self, username: str, password: str) -> bool:
        try:
            user = self.userDb.fetchUserByUsername(username)
            if not user:
                return False
            return user.checkPassword(password)
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return False
        return False

    @Slot(str, str, result=bool)
    def removeUserByUsername(self, username: str, password: str) -> bool:
        if (not self.authenticateUser(username, password)):
            print("Error deleting user: Incorrect password or username.")
            return False
        try:
            self.userDb.removeUserByUsername(username)
            self.usersCountChanged.emit()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        return False
        
    @Slot(result=bool)
    def removeUsers(self) -> bool:
        try:
            self.userDb.removeUsers()
            self.usersCountChanged.emit()
            return True
        except Exception as e:
            print(f"Error deleting all users: {e}")
            return False
        return False