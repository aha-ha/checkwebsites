from PyQt5 import QtWidgets, uic
import sys

from checker import WebserverChecker

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('checkwebsites.ui', self) # Load the .ui file
        self.connectSignalsSlots()


    def connectSignalsSlots(self):
        self.btn.clicked.connect(self.check_button_clicked)


    def check_button_clicked(self):
        print("Test gestartet!")
        print(self.url.text())
        self.prg.setValue(20)
        ws1 = WebserverChecker(self.url.text())
        self.prg.setValue(50)
        good, color, text = ws1.check()
        self.prg.setValue(99)
        self.url.setText(self.url.text() + " - " + text)
        self.prg.setValue(100)




        

app = QtWidgets.QApplication(sys.argv)
ui = Ui()

ui.show()
app.exec_()
