# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
# pyuic5 -x thuvien.ui -o thuvien.py

from PyQt5 import QtCore, QtGui, QtWidgets

from pythonProject.BTPy.QuanLyThuVien.dangki import Ui_dangki
from pythonProject.BTPy.QuanLyThuVien.login import Ui_login


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 941, 221))
        self.label.setStyleSheet("border-image: url(:/newPrefix/C:/Users/nguye/OneDrive/Pictures/Screenshots/Screenshot 2024-06-21 172614.png);\n"
"border-image: url(:/newPrefix/ảnh/Screenshot 2024-06-21 172614.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 190, 561, 201))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.label_2.setMouseTracking(False)
        self.label_2.setObjectName("label_2")
        self.btndki = QtWidgets.QPushButton(self.centralwidget)
        self.btndki.setGeometry(QtCore.QRect(110, 390, 181, 81))
        self.btndki.setObjectName("btndki")
        self.btndnhap = QtWidgets.QPushButton(self.centralwidget)
        self.btndnhap.setGeometry(QtCore.QRect(540, 380, 151, 81))
        self.btndnhap.setObjectName("btndnhap")
        self.label_2.raise_()
        self.label.raise_()
        self.btndki.raise_()
        self.btndnhap.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSkin1 = QtWidgets.QAction(MainWindow)
        self.actionSkin1.setObjectName("actionSkin1")
        self.actionSkin2 = QtWidgets.QAction(MainWindow)
        self.actionSkin2.setObjectName("actionSkin2")
        self.actionNone = QtWidgets.QAction(MainWindow)
        self.actionNone.setObjectName("actionNone")
        self.actionNone_2 = QtWidgets.QAction(MainWindow)
        self.actionNone_2.setObjectName("actionNone_2")
        self.menuFile.addAction(self.actionSkin1)
        self.menuFile.addAction(self.actionSkin2)
        self.menuFile.addAction(self.actionNone)
        self.menuHelp.addAction(self.actionNone_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btndnhap.clicked.connect(self.dangnhap)
        self.btndki.clicked.connect(self.dangki)

    def dangnhap(self):
        self.dangnhap_window = QtWidgets.QMainWindow()
        self.ui = Ui_login()
        self.ui.setupUi(self.dangnhap_window)
        self.dangnhap_window.show()

    def dangki(self):
        self.dangki_window = QtWidgets.QDialog()
        self.ui = Ui_dangki()
        self.ui.setupUi(self.dangki_window)
        self.dangki_window.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quản lý thư viện"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#0055ff;\">PHẦN MỀM QUẢN LÝ THƯ VIỆN</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "PHẦN MỀM QUẢN LÝ THƯ VIỆN"))
        self.btndki.setText(_translate("MainWindow", "Đăng kí"))
        self.btndnhap.setText(_translate("MainWindow", "Đăng nhập"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionSkin1.setText(_translate("MainWindow", "Skin1"))
        self.actionSkin2.setText(_translate("MainWindow", "Skin2"))
        self.actionNone.setText(_translate("MainWindow", "None"))
        self.actionNone_2.setText(_translate("MainWindow", "None"))
import imge

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
