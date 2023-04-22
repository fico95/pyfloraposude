from PySide2.QtCore import QObject, Signal, Slot, Property

from Users.User import User
from Users.UserDb import UserDb

class UserHandler(QObject):
    numUsersChanged = Signal()

    @Property(int, notify=numUsersChanged)
    def numUsers(self):
        return self.userDb.getNumUsers()

    def __init__(self, dbPath, parent=None):
        super().__init__(parent)
        self.userDb = UserDb(dbPath)

        numUsers = self.numUsers
        if numUsers > 1:
            print(f"Deleting {numUsers} users...")
            self.userDb.deleteAllUsers()

    @Slot(str, str, result=bool)
    def addUser(self, username, password):
        try:
            user = User(username, password)
            self.userDb.addUser(user)
            self.numUsersChanged.emit()
            return True
        except Exception as e:
            print(f"Error adding user: {e}")
            return False
        
    @Slot(str, str, str, result=bool)
    def updateUserPassword(self, username, oldPassword, newPassword):
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
    def authenticateUser(self, username, password):
        try:
            user = self.userDb.getUser(username)
            if not user:
                return False
            return user.checkPassword(password)
        except Exception as e:
            print(f"Error authenticating user: {e}")
            return False

    @Slot(str, str, result=bool)
    def deleteUser(self, username, password):
        print("WTF")
        if (not self.authenticateUser(username, password)):
            print("Error deleting user: Incorrect password or username.")
            return False
        try:
            self.userDb.deleteUser(username)
            self.numUsersChanged.emit()
            return True
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        
    @Slot(result=bool)
    def deleteAllUsers(self):
        try:
            self.userDb.deleteAllUsers()
            self.numUsersChanged.emit()
            return True
        except Exception as e:
            print(f"Error deleting all users: {e}")
            return False
        
    @Slot(result=bool)
    def userExists(self):
        return self.numUsers > 0
