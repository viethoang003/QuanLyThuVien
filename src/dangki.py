# -*- coding: utf-8 -*-
import mysql.connector
# Form implementation generated from reading ui file 'dangki.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_dangki(object):
    def setupUi(self, dangki):
        dangki.setObjectName("dangki")
        dangki.resize(400, 300)
        self.labeldk_tk = QtWidgets.QLabel(dangki)
        self.labeldk_tk.setGeometry(QtCore.QRect(50, 70, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labeldk_tk.setFont(font)
        self.labeldk_tk.setObjectName("labeldk_tk")
        self.label_2 = QtWidgets.QLabel(dangki)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.linedk_tk = QtWidgets.QLineEdit(dangki)
        self.linedk_tk.setGeometry(QtCore.QRect(150, 70, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.linedk_tk.setFont(font)
        self.linedk_tk.setInputMask("")
        self.linedk_tk.setText("")
        self.linedk_tk.setFrame(True)
        self.linedk_tk.setObjectName("linedk_tk")
        self.tieude2 = QtWidgets.QLabel(dangki)
        self.tieude2.setGeometry(QtCore.QRect(140, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft Sans Serif")
        font.setPointSize(15)
        self.tieude2.setFont(font)
        self.tieude2.setObjectName("tieude2")
        self.linedk_mk = QtWidgets.QLineEdit(dangki)
        self.linedk_mk.setGeometry(QtCore.QRect(150, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.linedk_mk.setFont(font)
        self.linedk_mk.setInputMask("")
        self.linedk_mk.setText("")
        self.linedk_mk.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linedk_mk.setObjectName("linedk_mk")
        self.btn_dki = QtWidgets.QPushButton(dangki)
        self.btn_dki.setGeometry(QtCore.QRect(30, 220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_dki.setFont(font)
        self.btn_dki.setObjectName("btn_dki")
        self.checkpass = QtWidgets.QCheckBox(dangki)
        self.checkpass.setGeometry(QtCore.QRect(70, 170, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkpass.setFont(font)
        self.checkpass.setObjectName("checkpass")
        self.btn_dki_2 = QtWidgets.QPushButton(dangki)
        self.btn_dki_2.setGeometry(QtCore.QRect(220, 220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_dki_2.setFont(font)
        self.btn_dki_2.setObjectName("btn_dki_2")

        self.retranslateUi(dangki)
        QtCore.QMetaObject.connectSlotsByName(dangki)
        self.btn_dki_2.clicked.connect(self.reset)
        self.checkpass.stateChanged.connect(self.hienpass)
        self.btn_dki.clicked.connect(self.dangki)
    def hienpass(self, state):
        if state == QtCore.Qt.Checked:
            self.linedk_mk.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.linedk_mk.setEchoMode(QtWidgets.QLineEdit.Password)
    def reset(self):
        self.linedk_tk.setText("")
        self.linedk_mk.setText("")
    def dangki(self):
        self.db = mysql.connector.connect(host="localhost", user="root", password="", database="qlthuvien")
        self.mycursor = self.db.cursor()
        taikhoan = self.linedk_tk.text()
        matkhau = self.linedk_mk.text()
        sql = "SELECT * FROM taikhoan WHERE taikhoan=%s AND matkhau=%s"
        self.mycursor.execute(sql, (taikhoan, matkhau))
        data = self.mycursor.fetchall()
        tb = QMessageBox()
        if data:
            tb.setWindowTitle("Lỗi")
            tb.setText("Tài khoản đã tồn tại")
            tb.exec_()
        else:
            sql = "INSERT INTO  taikhoan (taikhoan, matkhau) VALUES (%s, %s)"
            self.mycursor.execute(sql, (taikhoan, matkhau))
            self.db.commit()
            tb.setWindowTitle("Thành công")
            tb.setText("Đăng kí tài khoản thành công ")
            tb.exec_()
    def retranslateUi(self, dangki):
        _translate = QtCore.QCoreApplication.translate
        dangki.setWindowTitle(_translate("dangki", "Đăng kí"))
        self.labeldk_tk.setText(_translate("dangki", "Tài khoản"))
        self.label_2.setText(_translate("dangki", "Mật khẩu"))
        self.linedk_tk.setPlaceholderText(_translate("dangki", "Nhập tài khoản"))
        self.tieude2.setText(_translate("dangki", "Đăng kí"))
        self.linedk_mk.setPlaceholderText(_translate("dangki", "Nhập mật khẩu"))
        self.btn_dki.setText(_translate("dangki", "Đăng kí"))
        self.checkpass.setText(_translate("dangki", "Hiện mật khẩu"))
        self.btn_dki_2.setText(_translate("dangki", "Nhập lại"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dangki = QtWidgets.QDialog()
    ui = Ui_dangki()
    ui.setupUi(dangki)
    dangki.show()
    sys.exit(app.exec_())
