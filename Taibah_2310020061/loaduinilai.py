import sys
import mysql.connector
from PyQt5 import QtWidgets
from nilai import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

class NilaiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(NilaiApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Koneksi database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mahasiswa1"
        )
        self.cursor = self.db.cursor()

        # Event tombol
        self.ui.pushButton_tambah.clicked.connect(self.tambah_data)
        self.ui.pushButton_ubah.clicked.connect(self.ubah_data)
        self.ui.pushButton_hapus.clicked.connect(self.hapus_data)
        self.ui.pushButton_reset.clicked.connect(self.reset_form)
        self.ui.tableWidget.cellClicked.connect(self.load_data_ke_form)

        self.load_data_ke_tabel()

    def tambah_data(self):
        data = self.get_form_data(include_id=False)
        sql = """
        INSERT INTO nilai (id_mahasiswa, nilai_harian, nilai_tugas, nilai_uts, nilai_uas)
        VALUES (%s, %s, %s, %s, %s)
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
        UPDATE nilai SET 
            id_mahasiswa=%s,
            nilai_harian=%s,
            nilai_tugas=%s,
            nilai_uts=%s,
            nilai_uas=%s
        WHERE id=%s
        """
        try:
            self.cursor.execute(sql, data[1:] + data[0:1])  # id ditaruh di belakang
            self.db.commit()
            QMessageBox.information(self, "Berhasil", "Data berhasil diubah!")
            self.load_data_ke_tabel()
            self.reset_form()
        except Exception as e:
            QMessageBox.warning(self, "Gagal", f"Gagal mengubah data: {e}")

    def hapus_data(self):
        id = self.ui.lineEdit_id.text()
        if id == "":
            QMessageBox.warning(self, "Peringatan", "Pilih data yang ingin dihapus!")
            return
        sql = "DELETE FROM nilai WHERE id=%s"
        try:
            self.cursor.execute(sql, (id,))
            self.db.commit()
            QMessageBox.information(self, "Berhasil", "Data berhasil dihapus!")
            self.load_data_ke_tabel()
            self.reset_form()
        except Exception as e:
            QMessageBox.warning(self, "Gagal", f"Gagal menghapus data: {e}")

    def reset_form(self):
        self.ui.lineEdit_id.clear()
        self.ui.lineEdit_idmahasiswa.clear()
        self.ui.lineEdit_nilaiharian.clear()
        self.ui.lineEdit_nilaitugas.clear()
        self.ui.lineEdit_nilaiuts.clear()
        self.ui.lineEdit_nilaiuas.clear()

    def get_form_data(self, include_id=True):
        if include_id:
            return (
                self.ui.lineEdit_id.text(),
                self.ui.lineEdit_idmahasiswa.text(),
                self.ui.lineEdit_nilaiharian.text(),
                self.ui.lineEdit_nilaitugas.text(),
                self.ui.lineEdit_nilaiuts.text(),
                self.ui.lineEdit_nilaiuas.text()
            )
        else:
            return (
                self.ui.lineEdit_idmahasiswa.text(),
                self.ui.lineEdit_nilaiharian.text(),
                self.ui.lineEdit_nilaitugas.text(),
                self.ui.lineEdit_nilaiuts.text(),
                self.ui.lineEdit_nilaiuas.text()
            )

    def load_data_ke_tabel(self):
        self.cursor.execute("SELECT * FROM nilai")
        result = self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(len(result))
        self.ui.tableWidget.setColumnCount(6)
        for row_index, row_data in enumerate(result):
            for column_index, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))

    def load_data_ke_form(self, row):
        self.ui.lineEdit_id.setText(self.ui.tableWidget.item(row, 0).text())
        self.ui.lineEdit_idmahasiswa.setText(self.ui.tableWidget.item(row, 1).text())
        self.ui.lineEdit_nilaiharian.setText(self.ui.tableWidget.item(row, 2).text())
        self.ui.lineEdit_nilaitugas.setText(self.ui.tableWidget.item(row, 3).text())
        self.ui.lineEdit_nilaiuts.setText(self.ui.tableWidget.item(row, 4).text())
        self.ui.lineEdit_nilaiuas.setText(self.ui.tableWidget.item(row, 5).text())


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = NilaiApp()
    window.show()
    sys.exit(app.exec_())
