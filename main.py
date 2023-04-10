# This Python file uses the following encoding: utf-8

import sys

from application import Application
from users.userdatabase import UserDatabase
from users.user import User

if __name__ == "__main__":
    latitude = 45.8102
    longitude = 15.9411

    userDb = UserDatabase('test.db')
    userDb.add_user(User('test2', 'test'))
    sys.exit()

#    print (sensors.generate_random_data(latitude, longitude, 2))
    # latitude = 45.8102
    # longitude = 15.9411

    # temperature = temperature.get_temperature(latitude, longitude)

    # if temperature is not None:
    #     print(f"The temperature is {temperature} degrees Celsius.")
    # else:
    #     print("Failed to retrieve temperature data.")

    app = Application(sys.argv)

    sys.exit(app.exec_())
