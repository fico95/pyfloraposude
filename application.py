import os
from pathlib import Path
import sys

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

class Application(QGuiApplication):
    def __init__(self, *args, **kwargs):
        QGuiApplication.__init__(self, *args, **kwargs)

        self.engine = QQmlApplicationEngine()
        self.engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))
        if not self.engine.rootObjects():
            sys.exit(-1)