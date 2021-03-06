# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginp.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from welcomep import Ui_welcome
import sqlite3


class Ui_login(object):
    def showmessage(self,title,message):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
    def welcomewindows(self):
            self.welcomewindow=QtWidgets.QMainWindow()
            self.ui=Ui_welcome()
            self.ui.setupUi(self.welcomewindow)
            self.welcomewindow.show()
        
    def loginpage(self):
        username=self.lineEdit.text()
        password=self.lineEdit_2.text()
        conn=sqlite3.connect("p_db")
        result=conn.execute("select * from users where username=? and password=?",(username,password))
        if(len(result.fetchall())>0):
            print("user found:")
            self.welcomewindows()
        else:
            print("user not found!")
            self.showmessage('Warning','Invalid username and password')
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(830, 511)
        self.label = QtWidgets.QLabel(login)
        self.label.setGeometry(QtCore.QRect(0, 0, 861, 521))
        self.label.setStyleSheet("\n"
"background-color: rgb(0, 255, 255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/it/Downloads/2637581.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(login)
        self.label_2.setGeometry(QtCore.QRect(330, 40, 131, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(210, 220, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(login)
        self.label_4.setGeometry(QtCore.QRect(200, 280, 81, 21))
        self.label_4.setObjectName("label_4")
        self.lbttn = QtWidgets.QPushButton(login)
        self.lbttn.setGeometry(QtCore.QRect(350, 390, 141, 23))
        self.lbttn.setStyleSheet("background-color: rgb(85, 255, 255);")
        self.lbttn.setObjectName("lbttn")
        
        self.lbttn.clicked.connect(self.loginpage)
        
        self.lineEdit = QtWidgets.QLineEdit(login)
        self.lineEdit.setGeometry(QtCore.QRect(410, 210, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(login)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 290, 113, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.label_2.setText(_translate("login", "Welcome to our website"))
        self.label_3.setText(_translate("login", "Username"))
        self.label_4.setText(_translate("login", "Password"))
        self.lbttn.setText(_translate("login", "NEXT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QWidget()
    ui = Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
