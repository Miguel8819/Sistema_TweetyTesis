import sys
import os
from wsgiref.validate import validator

from pymysql import STRING
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.CreateProveedorController import CreateProveedorController
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Models.Proveedores import Proveedor
from Database.Connection import connection


class Ui_AgregarProducto(object):
    def __init__(self):
        self.create_proveedor_controller = CreateProveedorController(self)
        self.proveedor = Proveedor(connection())
    def setupUi(self, AgregarProducto):
        AgregarProducto.setObjectName("AgregarProducto")
        AgregarProducto.resize(594, 473)
        AgregarProducto.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label = QtWidgets.QLabel(AgregarProducto)
        self.label.setGeometry(QtCore.QRect(180, 30, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(AgregarProducto)
        self.tableWidget.setGeometry(QtCore.QRect(140, 80, 341, 321))
        self.tableWidget.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(10)
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
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.btnAgregar = QtWidgets.QPushButton(AgregarProducto)
        self.btnAgregar.setGeometry(QtCore.QRect(210, 410, 75, 23))
        self.btnAgregar.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.btnAgregar.setObjectName("btnAgregar")
        self.btnCancelar = QtWidgets.QPushButton(AgregarProducto)
        self.btnCancelar.setGeometry(QtCore.QRect(320, 410, 75, 23))
        self.btnCancelar.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.btnCancelar.setObjectName("btnCancelar")
        self.btn_verProductos = QtWidgets.QPushButton(AgregarProducto)
        self.btn_verProductos.setGeometry(QtCore.QRect(50, 80, 75, 23))
        self.btn_verProductos.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.btn_verProductos.setObjectName("btn_verProductos")

        self.retranslateUi(AgregarProducto)
        QtCore.QMetaObject.connectSlotsByName(AgregarProducto)

        self.a = self.btn_verProductos.clicked.connect(lambda:self.create_proveedor_controller.verProductos())
        self.b = self.btnAgregar.clicked.connect(lambda:self.create_proveedor_controller.ingresarProductoaProveedor())
        

    def retranslateUi(self, AgregarProducto):
        _translate = QtCore.QCoreApplication.translate
        AgregarProducto.setWindowTitle(_translate("AgregarProducto", "Agregar producto a proveedor"))
        self.label.setText(_translate("AgregarProducto", "LISTA DE PRODUCTOS"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("AgregarProducto", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("AgregarProducto", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("AgregarProducto", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("AgregarProducto", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("AgregarProducto", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("AgregarProducto", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("AgregarProducto", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("AgregarProducto", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("AgregarProducto", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("AgregarProducto", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("AgregarProducto", "codProducto"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("AgregarProducto", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("AgregarProducto", "Marca"))
        self.btnAgregar.setText(_translate("AgregarProducto", "Agregar"))
        self.btnCancelar.setText(_translate("AgregarProducto", "Cancelar"))
        self.btn_verProductos.setText(_translate("AgregarProducto", "Ver Productos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AgregarProducto = QtWidgets.QWidget()
    ui = Ui_AgregarProducto()
    ui.setupUi(AgregarProducto)
    AgregarProducto.show()
    sys.exit(app.exec_())
