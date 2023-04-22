import os
import signal

from pathlib import Path
import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtQuickControls2 import QQuickStyle

from users.userhandler import UserHandler
from stackcontroller import StackController

class Application(QGuiApplication):
    def __init__(self, *args, **kwargs):
        QGuiApplication.__init__(self, *args, **kwargs)
                
        signal.signal(signal.SIGTERM, self.sigterm_handler)

        self.engine = QQmlApplicationEngine()
        QQuickStyle.setStyle("Imagine")

        self.user_handler = UserHandler('test.db')
        self.stack_controller = StackController()

        self.engine.rootContext().setContextProperty("userHandler", self.user_handler)
        self.engine.rootContext().setContextProperty("stackController", self.stack_controller)

        self.engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
        if not self.engine.rootObjects():
            sys.exit(-1)

    def sigterm_handler(self, *args):
        QGuiApplication.quit()