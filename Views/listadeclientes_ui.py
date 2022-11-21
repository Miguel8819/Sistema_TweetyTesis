import sys
import os
from wsgiref.validate import validator

from pymysql import STRING
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.listarClienteController import listarClienteController
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QDoubleValidator, QValidator
from Models.cliente import Cliente

from PyQt5 import QtCore, QtGui, QtWidgets
from Database.Connection import connection

class Ui_lista_clientes(object):
    def __init__(self):
        self.listarclientecontroller = listarClienteController(self)
        self.cliente = Cliente(connection())
    def setupUi(self, lista_clientes):
        lista_clientes.setObjectName("lista_clientes")
        lista_clientes.resize(1107, 489)
        lista_clientes.setStyleSheet("\n"
"background-color: rgb(0, 165, 225);")
        self.tabWidget = QtWidgets.QTabWidget(lista_clientes)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1151, 581))
        self.tabWidget.setStyleSheet("\n"
"background-color: rgb(0, 165, 225);\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(30, 100, 1041, 271))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 229, 253);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
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
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(440, 30, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.boton_actualizar = QtWidgets.QPushButton(self.tab)
        self.boton_actualizar.setGeometry(QtCore.QRect(280, 400, 151, 23))
        self.boton_actualizar.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.boton_actualizar.setObjectName("boton_actualizar")
        self.boton_salir = QtWidgets.QPushButton(self.tab)
        self.boton_salir.setGeometry(QtCore.QRect(690, 400, 151, 23))
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
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 100, 1041, 271))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 229, 253);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(10)
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
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(370, 30, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.boton_actualizar2 = QtWidgets.QPushButton(self.tab_2)
        self.boton_actualizar2.setGeometry(QtCore.QRect(280, 410, 151, 23))
        self.boton_actualizar2.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.boton_actualizar2.setObjectName("boton_actualizar2")
        self.boton_darAlta = QtWidgets.QPushButton(self.tab_2)
        self.boton_darAlta.setGeometry(QtCore.QRect(480, 410, 151, 23))
        self.boton_darAlta.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.boton_darAlta.setObjectName("boton_darAlta")
        self.boton_salir_2 = QtWidgets.QPushButton(self.tab_2)
        self.boton_salir_2.setGeometry(QtCore.QRect(690, 410, 151, 23))
        self.boton_salir_2.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.boton_salir_2.setObjectName("boton_salir_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 91, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Imagenes/nook.jpg"))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(lista_clientes)
        self.tabWidget.setCurrentIndex(0) 
        QtCore.QMetaObject.connectSlotsByName(lista_clientes)

        self.a = self.boton_actualizar.clicked.connect(lambda:self.listarclientecontroller.listarClientesActivos())
        self.b = self.boton_actualizar2.clicked.connect(lambda:self.listarclientecontroller.listarBajaClientes())
        self.c = self.boton_salir.clicked.connect(lambda:self.listarclientecontroller.SalirA(lista_clientes))
        self.s = self.boton_salir_2.clicked.connect(lambda:self.listarclientecontroller.SalirA(lista_clientes))
        self.r = self.boton_darAlta.clicked.connect(lambda:self.listarclientecontroller.darAltaCliente())

    def retranslateUi(self, lista_clientes):
        _translate = QtCore.QCoreApplication.translate
        lista_clientes.setWindowTitle(_translate("lista_clientes", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("lista_clientes", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("lista_clientes", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("lista_clientes", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("lista_clientes", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("lista_clientes", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("lista_clientes", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("lista_clientes", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("lista_clientes", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("lista_clientes", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("lista_clientes", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("lista_clientes", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("lista_clientes", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("lista_clientes", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("lista_clientes", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("lista_clientes", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("lista_clientes", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("lista_clientes", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("lista_clientes", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("lista_clientes", "19"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("lista_clientes", "codCliente"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("lista_clientes", "nroDni"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("lista_clientes", "Apellido y Nombre"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("lista_clientes", "Fecha Alta"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("lista_clientes", "Calle"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("lista_clientes", "Nro de Calle"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("lista_clientes", "Ciudad"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("lista_clientes", "Codigo Postal"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("lista_clientes", "Telefono"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("lista_clientes", "Email"))
        self.label.setText(_translate("lista_clientes", "Clientes Activos"))
        self.boton_actualizar.setText(_translate("lista_clientes", "Actualizar"))
        self.boton_salir.setText(_translate("lista_clientes", "Salir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("lista_clientes", "Clientes Activos"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("lista_clientes", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("lista_clientes", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("lista_clientes", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("lista_clientes", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("lista_clientes", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("lista_clientes", "6"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("lista_clientes", "7"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("lista_clientes", "8"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("lista_clientes", "9"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("lista_clientes", "10"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("lista_clientes", "11"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("lista_clientes", "12"))
        item = self.tableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("lista_clientes", "13"))
        item = self.tableWidget_2.verticalHeaderItem(13)
        item.setText(_translate("lista_clientes", "14"))
        item = self.tableWidget_2.verticalHeaderItem(14)
        item.setText(_translate("lista_clientes", "15"))
        item = self.tableWidget_2.verticalHeaderItem(15)
        item.setText(_translate("lista_clientes", "16"))
        item = self.tableWidget_2.verticalHeaderItem(16)
        item.setText(_translate("lista_clientes", "17"))
        item = self.tableWidget_2.verticalHeaderItem(17)
        item.setText(_translate("lista_clientes", "18"))
        item = self.tableWidget_2.verticalHeaderItem(18)
        item.setText(_translate("lista_clientes", "19"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("lista_clientes", "codCliente"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("lista_clientes", "nroDni"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("lista_clientes", "Apellido y Nombre"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("lista_clientes", "Fecha de Baja"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("lista_clientes", "Calle"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("lista_clientes", "Nro de Calle"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("lista_clientes", "Ciudad"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("lista_clientes", "Codigo Postal"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("lista_clientes", "Telefono"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("lista_clientes", "Email"))
        self.label_2.setText(_translate("lista_clientes", "Clientes dados de baja"))
        self.boton_actualizar2.setText(_translate("lista_clientes", "Actualizar"))
        self.boton_darAlta.setText(_translate("lista_clientes", "Dar de Alta"))
        self.boton_salir_2.setText(_translate("lista_clientes", "Salir"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("lista_clientes", "Clientes dados de baja"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lista_clientes = QtWidgets.QWidget()
    ui = Ui_lista_clientes()
    ui.setupUi(lista_clientes)
    lista_clientes.show()
    sys.exit(app.exec_())
