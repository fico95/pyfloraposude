import os
import signal

from pathlib import Path
import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

from users.userhandler import UserHandler

class Application(QGuiApplication):
    def __init__(self, *args, **kwargs):
        QGuiApplication.__init__(self, *args, **kwargs)

        signal.signal(signal.SIGTERM, self.sigterm_handler)

        self.engine = QQmlApplicationEngine()

        self.user_handler = UserHandler('test.db')

        self.engine.rootContext().setContextProperty("userHandler", self.user_handler)

        self.engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
        if not self.engine.rootObjects():
            sys.exit(-1)

    def sigterm_handler(self, *args):
        QGuiApplication.quit()