import sys
import mysql.connector
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1307, 913)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 1271, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setText("MAHASISWA")

        # Label dan input
        labels = ["Npm", "Nama Lengkap", "Nama Panggilan", "No HP", "Email",
                "Kelas", "Matkul", "Prodi", "Lokasi Kampus"]
        self.lineEdits = []
        for i, text in enumerate(labels):
            label = QtWidgets.QLabel(Form)
            label.setGeometry(QtCore.QRect(60, 60 + (i * 40), 131, 16))
            label.setText(text)

            lineEdit = QtWidgets.QLineEdit(Form)
            lineEdit.setGeometry(QtCore.QRect(230, 60 + (i * 40), 171, 22))
            self.lineEdits.append(lineEdit)

        # Tombol
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(50, 490, 131, 41))
        self.pushButton.setText("Tambah")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 490, 131, 41))
        self.pushButton_2.setText("Ubah")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 490, 131, 41))
        self.pushButton_3.setText("Hapus")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 560, 131, 41))
        self.pushButton_4.setText("Batal")

        # Tabel
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(90, 650, 1131, 201))
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels(labels)
        self.tableWidget.setRowCount(0)

class FormApp(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Koneksi ke MySQL
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mahasiswa1"
        )
        self.cursor = self.db.cursor()

        # Event tombol
        self.pushButton.clicked.connect(self.tambah_data)
        self.pushButton_2.clicked.connect(self.ubah_data)
        self.pushButton_3.clicked.connect(self.hapus_data)
        self.pushButton_4.clicked.connect(self.batal_input)
        self.tableWidget.cellClicked.connect(self.isi_form_dari_tabel)

        self.load_data_ke_tabel()

    def tambah_data(self):
        data = [e.text() for e in self.lineEdits]
        try:
            sql = """
            INSERT INTO mahasiswaaa 
            (npm, nama_lengkap, nama_panggilan, no_hp, email, kelas, matakuliah, prodi, lokasi_kampus)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(sql, tuple(data))
            self.db.commit()
            QMessageBox.information(self, "Berhasil", "Data berhasil ditambahkan!")
            self.load_data_ke_tabel()
            self.batal_input()
        except Exception as e:
            QMessageBox.warning(self, "Gagal", f"Error: {e}")

    def ubah_data(self):
        data = [e.text() for e in self.lineEdits]
        try:
            sql = """
            UPDATE mahasiswaaa SET 
            nama_lengkap=%s, nama_panggilan=%s, no_hp=%s, email=%s,
            kelas=%s, matakuliah=%s, prodi=%s, lokasi_kampus=%s
            WHERE npm=%s
            """
            self.cursor.execute(sql, tuple(data[1:] + [data[0]]))
            self.db.commit()
            QMessageBox.information(self, "Berhasil", "Data berhasil diubah!")
            self.load_data_ke_tabel()
            self.batal_input()
        except Exception as e:
            QMessageBox.warning(self, "Gagal", f"Error: {e}")

    def hapus_data(self):
        npm = self.lineEdits[0].text()
        try:
            sql = "DELETE FROM mahasiswaaa WHERE npm=%s"
            self.cursor.execute(sql, (npm,))
            self.db.commit()
            QMessageBox.information(self, "Berhasil", "Data berhasil dihapus!")
            self.load_data_ke_tabel()
            self.batal_input()
        except Exception as e:
            QMessageBox.warning(self, "Gagal", f"Error: {e}")

    def batal_input(self):
        for field in self.lineEdits:
            field.clear()

    def isi_form_dari_tabel(self, row):
        for i in range(9):
            item = self.tableWidget.item(row, i)
            self.lineEdits[i].setText(item.text() if item else "")

    def load_data_ke_tabel(self):
        self.cursor.execute("SELECT * FROM mahasiswaaa")
        results = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, value in enumerate(row_data):
                self.tableWidget.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(value)))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormApp()
    window.show()
    sys.exit(app.exec_())
