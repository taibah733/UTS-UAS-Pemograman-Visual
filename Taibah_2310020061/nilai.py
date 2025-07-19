from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1306, 910)
        self._setPalette(MainWindow)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Input Fields
        self.lineEdit_id = self._createLineEdit(260, 70)
        self.lineEdit_idmahasiswa = self._createLineEdit(260, 140)
        self.lineEdit_nilaiharian = self._createLineEdit(260, 210)
        self.lineEdit_nilaitugas = self._createLineEdit(260, 280)
        self.lineEdit_nilaiuts = self._createLineEdit(260, 350)
        self.lineEdit_nilaiuas = self._createLineEdit(260, 420)

        # Buttons
        self.pushButton_tambah = self._createButton("Tambah Data", 80, 510)
        self.pushButton_hapus = self._createButton("Hapus Data", 260, 510)
        self.pushButton_reset = self._createButton("Reset", 80, 600)
        self.pushButton_ubah = self._createButton("Ubah Data", 260, 600)

        # Table
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(440, 510, 751, 341))
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        headers = ["id", "id mahasiswa", "nilai harian", "nilai tugas", "nilai uts", "nilai uas"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem()
            item.setText(header)
            self.tableWidget.setHorizontalHeaderItem(i, item)

        # Labels
        self._createLabel("Id", 80, 70)
        self._createLabel("Id Mahasiswa", 80, 140)
        self._createLabel("Nilai Harian", 80, 210)
        self._createLabel("Nilai Tugas", 80, 280)
        self._createLabel("Nilai UTS", 80, 350)
        self._createLabel("Nilai UAS", 80, 420)

        self._createTitleLabel("Input Nilai Mahasiswa", 80, 10)
        self._createTitleLabel("Data Nilai", 750, 440)

        MainWindow.setCentralWidget(self.centralwidget)
        self._setupMenubarStatusbar(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _createLineEdit(self, x, y):
        line_edit = QtWidgets.QLineEdit(self.centralwidget)
        line_edit.setGeometry(QtCore.QRect(x, y, 151, 41))
        return line_edit

    def _createButton(self, text, x, y):
        button = QtWidgets.QPushButton(self.centralwidget)
        button.setGeometry(QtCore.QRect(x, y, 151, 61))
        button.setText(text)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        button.setFont(font)
        return button

    def _createLabel(self, text, x, y):
        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(x, y, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        label.setText(text)

    def _createTitleLabel(self, text, x, y):
        label = QtWidgets.QLabel(self.centralwidget)
        label.setGeometry(QtCore.QRect(x, y, 331 if x == 80 else 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        label.setFont(font)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.WindowText, brush)
        label.setPalette(palette)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setText(text)

    def _setPalette(self, MainWindow):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        for role in [QtGui.QPalette.Button, QtGui.QPalette.Light]:
            palette.setBrush(QtGui.QPalette.Active, role, brush)
            palette.setBrush(QtGui.QPalette.Inactive, role, brush)
            palette.setBrush(QtGui.QPalette.Disabled, role, brush)
        MainWindow.setPalette(palette)

    def _setupMenubarStatusbar(self, MainWindow):
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1306, 26))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
