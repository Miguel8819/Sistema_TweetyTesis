import sys
import os
from wsgiref.validate import validator

from pymysql import STRING
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.listarProveedoresController import listarProveedoresController
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QDoubleValidator, QValidator
from Models.Proveedores import Proveedor

from PyQt5 import QtCore, QtGui, QtWidgets
from Database.Connection import connection

class Ui_lista_proveedores(object):
    def __init__(self):
        self.listarproveedorescontroller = listarProveedoresController(self)
        self.proveedor = Proveedor(connection())
    def setupUi(self, lista_proveedores):
        lista_proveedores.setObjectName("lista_proveedores")
        lista_proveedores.resize(1386, 489)
        lista_proveedores.setStyleSheet("\n"
"background-color: rgb(0, 165, 225);")
        self.tabWidget = QtWidgets.QTabWidget(lista_proveedores)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1331, 581))
        self.tabWidget.setStyleSheet("\n"
"background-color: rgb(0, 165, 225);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 1241, 271))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 229, 253);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(12)
        self.tableWidget.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(540, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.boton_actualizar = QtWidgets.QPushButton(self.tab)
        self.boton_actualizar.setGeometry(QtCore.QRect(420, 400, 151, 23))
        self.boton_actualizar.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.boton_actualizar.setObjectName("boton_actualizar")
        self.boton_salir = QtWidgets.QPushButton(self.tab)
        self.boton_salir.setGeometry(QtCore.QRect(750, 400, 151, 23))
        self.boton_salir.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.boton_salir.setObjectName("boton_salir")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 91, 81))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Imagenes/ok.jpg"))
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(490, 20, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.boton_actualizar2 = QtWidgets.QPushButton(self.tab_2)
        self.boton_actualizar2.setGeometry(QtCore.QRect(380, 400, 151, 23))
        self.boton_actualizar2.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.boton_actualizar2.setObjectName("boton_actualizar2")
        self.boton_darAlta = QtWidgets.QPushButton(self.tab_2)
        self.boton_darAlta.setGeometry(QtCore.QRect(580, 400, 151, 23))
        self.boton_darAlta.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.boton_darAlta.setObjectName("boton_darAlta")
        self.boton_salir_2 = QtWidgets.QPushButton(self.tab_2)
        self.boton_salir_2.setGeometry(QtCore.QRect(790, 400, 151, 23))
        self.boton_salir_2.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.boton_salir_2.setObjectName("boton_salir_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 91, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Imagenes/nook.jpg"))
        self.label_4.setObjectName("label_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 100, 1251, 271))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 229, 253);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(12)
        self.tableWidget_2.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(11, item)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(lista_proveedores)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(lista_proveedores)

        self.a = self.boton_actualizar.clicked.connect(lambda:self.listarproveedorescontroller.listarProveedoresActivos())
        self.b = self.boton_actualizar2.clicked.connect(lambda:self.listarproveedorescontroller.listarBajaProveedores())
        self.c = self.boton_salir.clicked.connect(lambda:self.listarproveedorescontroller.SalirA(lista_proveedores))
        self.s = self.boton_salir_2.clicked.connect(lambda:self.listarproveedorescontroller.SalirA(lista_proveedores))
        self.r = self.boton_darAlta.clicked.connect(lambda:self.listarproveedorescontroller.darAltaProveedor())


    def retranslateUi(self, lista_proveedores):
        _translate = QtCore.QCoreApplication.translate
        lista_proveedores.setWindowTitle(_translate("lista_proveedores", "Lista de proveedores"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("lista_proveedores", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("lista_proveedores", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("lista_proveedores", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("lista_proveedores", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("lista_proveedores", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("lista_proveedores", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("lista_proveedores", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("lista_proveedores", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("lista_proveedores", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("lista_proveedores", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("lista_proveedores", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("lista_proveedores", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("lista_proveedores", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("lista_proveedores", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("lista_proveedores", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("lista_proveedores", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("lista_proveedores", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("lista_proveedores", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("lista_proveedores", "19"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("lista_proveedores", "codProveedores"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("lista_proveedores", "nro Cuil/Cuit"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("lista_proveedores", "Apellido y Nombre"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("lista_proveedores", "Nombre Factura"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("lista_proveedores", "Fecha Alta"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("lista_proveedores", "Calle"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("lista_proveedores", "Nro de Calle"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("lista_proveedores", "Ciudad"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("lista_proveedores", "Codigo Postal"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("lista_proveedores", "Telefono"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("lista_proveedores", "Email"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("lista_proveedores", "Pag. Web"))
        self.label.setText(_translate("lista_proveedores", "Proveedores Activos"))
        self.boton_actualizar.setText(_translate("lista_proveedores", "Actualizar"))
        self.boton_salir.setText(_translate("lista_proveedores", "Salir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("lista_proveedores", "Proveedores Activos"))
        self.label_2.setText(_translate("lista_proveedores", "Proveedores dados de baja"))
        self.boton_actualizar2.setText(_translate("lista_proveedores", "Actualizar"))
        self.boton_darAlta.setText(_translate("lista_proveedores", "Dar de Alta"))
        self.boton_salir_2.setText(_translate("lista_proveedores", "Salir"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("lista_proveedores", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("lista_proveedores", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("lista_proveedores", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("lista_proveedores", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("lista_proveedores", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("lista_proveedores", "6"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("lista_proveedores", "7"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("lista_proveedores", "8"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("lista_proveedores", "9"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("lista_proveedores", "10"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("lista_proveedores", "11"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("lista_proveedores", "12"))
        item = self.tableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("lista_proveedores", "13"))
        item = self.tableWidget_2.verticalHeaderItem(13)
        item.setText(_translate("lista_proveedores", "14"))
        item = self.tableWidget_2.verticalHeaderItem(14)
        item.setText(_translate("lista_proveedores", "15"))
        item = self.tableWidget_2.verticalHeaderItem(15)
        item.setText(_translate("lista_proveedores", "16"))
        item = self.tableWidget_2.verticalHeaderItem(16)
        item.setText(_translate("lista_proveedores", "17"))
        item = self.tableWidget_2.verticalHeaderItem(17)
        item.setText(_translate("lista_proveedores", "18"))
        item = self.tableWidget_2.verticalHeaderItem(18)
        item.setText(_translate("lista_proveedores", "19"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("lista_proveedores", "codProveedores"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("lista_proveedores", "nro Cuil/Cuit"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("lista_proveedores", "Apellido y Nombre"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("lista_proveedores", "Nombre Factura"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("lista_proveedores", "Fecha Alta"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("lista_proveedores", "Calle"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("lista_proveedores", "Nro de Calle"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("lista_proveedores", "Ciudad"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("lista_proveedores", "Codigo Postal"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("lista_proveedores", "Telefono"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("lista_proveedores", "Email"))
        item = self.tableWidget_2.horizontalHeaderItem(11)
        item.setText(_translate("lista_proveedores", "Pag. Web"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("lista_proveedores", "Proveedores dados de baja"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lista_proveedores = QtWidgets.QWidget()
    ui = Ui_lista_proveedores()
    ui.setupUi(lista_proveedores)
    lista_proveedores.show()
    sys.exit(app.exec_())
