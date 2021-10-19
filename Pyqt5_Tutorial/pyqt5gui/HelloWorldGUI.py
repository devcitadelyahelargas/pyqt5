import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QStackedWidget


class welcomeScreen(QDialog):
    def __init__(self):
        super(welcomeScreen, self).__init__()
        loadUi("welcome.ui", self)
        self.Continue.clicked.connect(self.Continue_ButtonFunc)

    def Continue_ButtonFunc(self):
        EnteredName = self.UserName.text()
        print(EnteredName)
        self.Name_Output.setText(f'Welcome {EnteredName} !')


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