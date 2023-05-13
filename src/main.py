import sys
import signal

import IconsResources
from Application import Application

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = Application(sys.argv)
    if (app.initialized):
        app.exec_()