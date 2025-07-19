from PyQt5 import QtWidgets, uic
import sys

app = QtWidgets.QApplication([])
win = uic.loadUi("2310020061taibah.ui")
win.show()

sys.exit(app.exec())