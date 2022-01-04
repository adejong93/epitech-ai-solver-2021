import sys
#import fire
from PyQt5.QtWidgets import QApplication

from src.gui.start_window import StartWindow


if __name__ == '__main__':
    app = QApplication.instance()

    if not app:
        app = QApplication(sys.argv)
    #fire.Fire()
    window = StartWindow()
    window.show()
    app.exec_()