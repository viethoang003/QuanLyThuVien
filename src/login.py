# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox

from pythonProject.BTPy.QuanLyThuVien.thuvien import Ui_MainWindow


class Ui_login(object):
    def setupUi(self, login):
        self.login_window = login  # Lưu tham chiếu đến cửa sổ đăng nhập
        login.setObjectName("login")
        login.setEnabled(True)
        login.resize(431, 304)
        font = QtGui.QFont()
        font.setPointSize(10)
        login.setFont(font)
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.labeltk = QtWidgets.QLabel(self.centralwidget)
        self.labeltk.setGeometry(QtCore.QRect(50, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labeltk.setFont(font)
        self.labeltk.setObjectName("labeltk")
        self.labemk = QtWidgets.QLabel(self.centralwidget)
        self.labemk.setGeometry(QtCore.QRect(50, 130, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labemk.setFont(font)
        self.labemk.setObjectName("labemk")
        self.btndangnhap = QtWidgets.QPushButton(self.centralwidget)
        self.btndangnhap.setGeometry(QtCore.QRect(60, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btndangnhap.setFont(font)
        self.btndangnhap.setObjectName("btndangnhap")
        self.checkpass = QtWidgets.QCheckBox(self.centralwidget)
        self.checkpass.setGeometry(QtCore.QRect(70, 180, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkpass.setFont(font)
        self.checkpass.setObjectName("checkpass")
        self.linetaikhoan = QtWidgets.QLineEdit(self.centralwidget)
        self.linetaikhoan.setGeometry(QtCore.QRect(150, 80, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.linetaikhoan.setFont(font)
        self.linetaikhoan.setInputMask("")
        self.linetaikhoan.setText("")
        self.linetaikhoan.setFrame(True)
        self.linetaikhoan.setObjectName("linetaikhoan")
        self.linepass = QtWidgets.QLineEdit(self.centralwidget)
        self.linepass.setGeometry(QtCore.QRect(150, 130, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.linepass.setFont(font)
        self.linepass.setInputMask("")
        self.linepass.setText("")
        self.linepass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linepass.setObjectName("linepass")
        self.tieude1 = QtWidgets.QLabel(self.centralwidget)
        self.tieude1.setGeometry(QtCore.QRect(140, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.tieude1.setFont(font)
        self.tieude1.setObjectName("tieude1")
        self.btndangnhap_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btndangnhap_2.setGeometry(QtCore.QRect(250, 230, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btndangnhap_2.setFont(font)
        self.btndangnhap_2.setObjectName("btndangnhap_2")

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)
        self.checkpass.stateChanged.connect(self.hienpass)
        self.btndangnhap.clicked.connect(self.dangnhap)
        self.btndangnhap_2.clicked.connect(self.reset)

    def hienpass(self, state):
        if state == QtCore.Qt.Checked:
            self.linepass.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.linepass.setEchoMode(QtWidgets.QLineEdit.Password)

    def dangnhap(self):
        self.db = mysql.connector.connect(host="localhost", user="root", password="", database="qlthuvien")
        self.mycursor = self.db.cursor()
        taikhoan = self.linetaikhoan.text()
        matkhau = self.linepass.text()
        sql = "SELECT * FROM taikhoan WHERE taikhoan=%s AND matkhau=%s"
        self.mycursor.execute(sql, (taikhoan, matkhau))
        data = self.mycursor.fetchall()
        tb = QMessageBox()
        if data:
            tb.setWindowTitle("Thành công")
            tb.setText("Đăng nhập thành công")
            tb.exec_()
            self.mo()
        else:
            tb.setIcon(QMessageBox.Warning)
            tb.setWindowTitle("Lỗi")
            tb.setText("Tài khoản hoặc mật khẩu không đúng!")
            tb.exec_()
            self.reset()
        self.db.close()

    def mo(self):
        self.thuvien_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.thuvien_window)
        self.thuvien_window.show()
        self.ui.xulybtn()
        self.ui.hien_tac_gia()
        self.ui.hien_sach()
        self.ui.hien_nhaxb()
        self.ui.hien_the_loai()
        self.ui.hien_tacgia_combobox()
        self.ui.hien_nhaxb_combobox()
        self.ui.hien_theloai_combobox()
        self.ui.hien_khach_hang()
        self.ui.hien_muontra()
        self.ui.thong_ke()
        self.login_window.close()

    def reset(self):
        self.linetaikhoan.setText("")
        self.linepass.setText("")
        self.tieude1.setText("Đăng nhập")

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Đăng nhập"))
        self.labeltk.setText(_translate("login", "Tài khoản"))
        self.labemk.setText(_translate("login", "Mật khẩu"))
        self.btndangnhap.setText(_translate("login", "Đăng nhập"))
        self.checkpass.setText(_translate("login", "Hiện mật khẩu"))
        self.linetaikhoan.setPlaceholderText(_translate("login", "Nhập tài khoản"))
        self.linepass.setPlaceholderText(_translate("login", "Nhập mật khẩu"))
        self.tieude1.setText(_translate("login", "Đăng nhập"))
        self.btndangnhap_2.setText(_translate("login", "Nhập lại"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()  # Sử dụng QMainWindow thay vì QWidget
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
