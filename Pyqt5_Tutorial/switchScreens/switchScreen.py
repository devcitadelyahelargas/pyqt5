import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QStackedWidget


class welcomeScreen(QDialog):
    def __init__(self):
        super(welcomeScreen, self).__init__()
        loadUi("welcome.ui", self)
        self.Next_Page.clicked.connect(self.Next_PageFunc)

    def Next_PageFunc(self):
        nextpage = nextPageScreen()
        widget.addWidget(nextpage)
        widget.setCurrentIndex(widget.currentIndex()+1)


class nextPageScreen(QDialog):
    def __init__(self):
        super(nextPageScreen, self).__init__()
        loadUi("nextpage.ui", self)
        self.Go_Back.clicked.connect(self.GoBackFunc)

    def GoBackFunc(self):
        widget.setCurrentIndex(widget.currentIndex()-1)


app = QApplication(sys.argv)
welcome = welcomeScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(1081)
widget.setFixedHeight(801)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting")