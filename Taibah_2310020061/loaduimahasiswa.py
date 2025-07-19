import sys
import mysql.connector
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

class MahasiswaApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MahasiswaApp, self).__init__()
        uic.loadUi("mahasiswaa.ui", self)

        # Koneksi database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="mahasiswa1"
        )
        self.cursor = self.db.cursor()

        # Tombol fungsi
        self.pushButton_tambah.clicked.connect(self.tambah_data)
        self.pushButton_ubah.clicked.connect(self.ubah_data)
        self.pushButton_hapus.clicked.connect(self.hapus_data)
        self.pushButton_batal.clicked.connect(self.reset_form)

        self.tableWidget.cellClicked.connect(self.load_data_ke_form)

        self.load_data_ke_tabel()

    def tambah_data(self):
        data = self.get_form_data()
        sql = """
        INSERT INTO mahasiswa 
        (npm, nama_lengkap, nama_panggilan, no_hp, email, kelas, matkul, prodi, lokasi_kampus)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(sql, data)
            self.db.commit()
            QMessageBox.information(self, "Berhasil", "Data berhasil ditambahkan!")
            self.load_data_ke_tabel()
            self.reset_form()
        except Exception as e:
            QMessageBox.warning(self, "Gagal", f"Gagal menambahkan data: {e}")

    def ubah_data(self):
        data = self.get_form_data()
        sql = """
        UPDATE mahasiswa SET 
            nama_lengkap=%s, nama_panggilan=%s, telepon=%s, email=%s, 
            kelas=%s, matkul=%s, prodi=%s, lokasi_kampus=%s
        WHERE npm=%s
        """
        try:
            self.cursor.execute(sql, data[1:] + data[0:1])
            self.db.commit()
            QMessageBox.information(self, "Berhasil", "Data berhasil diubah!")
            self.load_data_ke_tabel()
            self.reset_form()
        except Exception as e:
            QMessageBox.warning(self, "Gagal", f"Gagal mengubah data: {e}")

    def hapus_data(self):
        npm = self.lineEdit.text()
        if npm == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus!")
            return
        sql = "DELETE FROM mahasiswa WHERE npm=%s"
        try:
            self.cursor.execute(sql, (npm,))
            self.db.commit()
            QMessageBox.information(self, "Berhasil", "Data berhasil dihapus!")
            self.load_data_ke_tabel()
            self.reset_form()
        except Exception as e:
            QMessageBox.warning(self, "Gagal", f"Gagal menghapus data: {e}")

    def reset_form(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()
        self.lineEdit_9.clear()


    def get_form_data(self):
        return (
            self.lineEdit.text(),
            self.lineEdit_2.text(),
            self.lineEdit_3.text(),
            self.lineEdit_4.text(),
            self.lineEdit_5.text(),
            self.lineEdit_6.text(),
            self.lineEdit_7.text(),
            self.lineEdit_8.text(),
            self.lineEdit_9.text()
        )


    def load_data_ke_tabel(self):
        self.cursor.execute("SELECT * FROM mahasiswa")
        result = self.cursor.fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels([
            "npm", "nama lengkap", "nama panggilan", "no hp",
            "email", "kelas", "matkul", "prodi", "lokasi kampus"
        ])
        for row_index, row_data in enumerate(result):
            for column_index, data in enumerate(row_data):
                self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))

    def load_data_ke_form(self, row):
        self.lineEdit.setText(self.tableWidget.item(row, 0).text())
        self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())
        self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())
        self.lineEdit_4.setText(self.tableWidget.item(row, 3).text())
        self.lineEdit_5.setText(self.tableWidget.item(row, 4).text())
        self.lineEdit_6.setText(self.tableWidget.item(row, 5).text())
        self.lineEdit_7.setText(self.tableWidget.item(row, 6).text())
        self.lineEdit_8.setText(self.tableWidget.item(row, 7).text())
        self.lineEdit_9.setText(self.tableWidget.item(row, 8).text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MahasiswaApp()
    window.show()
    sys.exit(app.exec_())
