import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
from wsgiref.validate import validator
from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Product import Product

from createproduct_ui import Ui_CreateProduct
from Controllers.controlstockController import controlstockController
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QRegExpValidator, QDoubleValidator, QValidator
from Database.Connection import connection

class Ui_listaDeProductos(object):
    def __init__(self):
        self.controlstock_controller = controlstockController(self)
        self.productos = Product(connection())
    def setupUi(self, listaDeProductos):
        #Validador de input en int
        intValidator = QRegExpValidator(QRegExp(r'[0-9\s]+'))
        
        #Validador de input string
        stringValidator = QRegExpValidator(QRegExp(r'[a-zA-Z\s]+')) 
        listaDeProductos.setObjectName("listaDeProductos")
        listaDeProductos.resize(1324, 683)
        listaDeProductos.setStyleSheet("background-color: rgb(56, 213, 203);")
        self.tabWidget = QtWidgets.QTabWidget(listaDeProductos)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1321, 701))
        self.tabWidget.setStyleSheet("background-color: rgb(56, 213, 203);")
        self.tabWidget.setObjectName("tabWidget")
        self.ProductosActivos = QtWidgets.QWidget()
        self.ProductosActivos.setObjectName("ProductosActivos")
        self.label = QtWidgets.QLabel(self.ProductosActivos)
        self.label.setGeometry(QtCore.QRect(550, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.ProductosActivos)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.input_codigo = QtWidgets.QLineEdit(self.ProductosActivos)
        self.input_codigo.setGeometry(QtCore.QRect(40, 130, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_codigo.setFont(font)
        self.input_codigo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_codigo.setMaxLength(15)
        self.input_codigo.setObjectName("input_codigo")
        self.input_prod = QtWidgets.QLineEdit(self.ProductosActivos)
        self.input_prod.setGeometry(QtCore.QRect(210, 130, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_prod.setFont(font)
        self.input_prod.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_prod.setMaxLength(20)
        self.input_prod.setObjectName("input_prod")
        self.btn_buscar = QtWidgets.QPushButton(self.ProductosActivos)
        self.btn_buscar.setGeometry(QtCore.QRect(390, 130, 75, 21))
        self.btn_buscar.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.table_product = QtWidgets.QTableWidget(self.ProductosActivos)
        self.table_product.setEnabled(True)
        self.table_product.setGeometry(QtCore.QRect(20, 180, 1281, 351))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_product.sizePolicy().hasHeightForWidth())
        self.table_product.setSizePolicy(sizePolicy)
        self.table_product.setMinimumSize(QtCore.QSize(740, 350))
        self.table_product.setStyleSheet("background-color: rgb(172, 242, 255);")
        self.table_product.setMidLineWidth(1)
        self.table_product.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_product.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_product.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_product.setRowCount(20)
        self.table_product.setColumnCount(13)
        self.table_product.setObjectName("table_product")
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_product.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product.setHorizontalHeaderItem(12, item)
        self.table_product.horizontalHeader().setCascadingSectionResizes(False)
        self.table_product.horizontalHeader().setDefaultSectionSize(95)
        self.table_product.horizontalHeader().setMinimumSectionSize(30)
        self.table_product.verticalHeader().setDefaultSectionSize(30)
        self.label_3 = QtWidgets.QLabel(self.ProductosActivos)
        self.label_3.setGeometry(QtCore.QRect(210, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btn_actualizar = QtWidgets.QPushButton(self.ProductosActivos)
        self.btn_actualizar.setGeometry(QtCore.QRect(430, 560, 131, 30))
        self.btn_actualizar.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_actualizar.setFont(font)
        self.btn_actualizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_actualizar.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.btn_create = QtWidgets.QPushButton(self.ProductosActivos)
        self.btn_create.setGeometry(QtCore.QRect(580, 560, 131, 30))
        self.btn_create.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_create.setObjectName("btn_create")
        self.btn_volver = QtWidgets.QPushButton(self.ProductosActivos)
        self.btn_volver.setGeometry(QtCore.QRect(730, 560, 140, 31))
        self.btn_volver.setMinimumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_volver.setFont(font)
        self.btn_volver.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_volver.setObjectName("btn_volver")
        self.btn_limpiar = QtWidgets.QPushButton(self.ProductosActivos)
        self.btn_limpiar.setGeometry(QtCore.QRect(480, 130, 75, 21))
        self.btn_limpiar.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.tabWidget.addTab(self.ProductosActivos, "")
        self.ProductosDadosDeBaja = QtWidgets.QWidget()
        self.ProductosDadosDeBaja.setObjectName("ProductosDadosDeBaja")
        self.input_prod_2 = QtWidgets.QLineEdit(self.ProductosDadosDeBaja)
        self.input_prod_2.setGeometry(QtCore.QRect(210, 130, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_prod_2.setFont(font)
        self.input_prod_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_prod_2.setMaxLength(20)
        self.input_prod_2.setObjectName("input_prod_2")
        self.btn_volver_2 = QtWidgets.QPushButton(self.ProductosDadosDeBaja)
        self.btn_volver_2.setGeometry(QtCore.QRect(720, 560, 141, 31))
        self.btn_volver_2.setMinimumSize(QtCore.QSize(140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_volver_2.setFont(font)
        self.btn_volver_2.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_volver_2.setObjectName("btn_volver_2")
        self.label_4 = QtWidgets.QLabel(self.ProductosDadosDeBaja)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btn_actualizar_2 = QtWidgets.QPushButton(self.ProductosDadosDeBaja)
        self.btn_actualizar_2.setGeometry(QtCore.QRect(430, 560, 121, 30))
        self.btn_actualizar_2.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_actualizar_2.setFont(font)
        self.btn_actualizar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_actualizar_2.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_actualizar_2.setObjectName("btn_actualizar_2")
        self.input_codigo_2 = QtWidgets.QLineEdit(self.ProductosDadosDeBaja)
        self.input_codigo_2.setGeometry(QtCore.QRect(40, 130, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_codigo_2.setFont(font)
        self.input_codigo_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_codigo_2.setMaxLength(15)
        self.input_codigo_2.setObjectName("input_codigo_2")
        self.label_5 = QtWidgets.QLabel(self.ProductosDadosDeBaja)
        self.label_5.setGeometry(QtCore.QRect(210, 100, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.ProductosDadosDeBaja)
        self.label_6.setGeometry(QtCore.QRect(490, 30, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.table_product_2 = QtWidgets.QTableWidget(self.ProductosDadosDeBaja)
        self.table_product_2.setEnabled(True)
        self.table_product_2.setGeometry(QtCore.QRect(20, 180, 1281, 351))
        self.table_product_2.setMinimumSize(QtCore.QSize(740, 350))
        self.table_product_2.setStyleSheet("background-color: rgb(172, 242, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.table_product_2.setMidLineWidth(1)
        self.table_product_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.table_product_2.setRowCount(20)
        self.table_product_2.setObjectName("table_product_2")
        self.table_product_2.setColumnCount(12)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.table_product_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_product_2.setHorizontalHeaderItem(11, item)
        self.table_product_2.horizontalHeader().setCascadingSectionResizes(False)
        self.table_product_2.horizontalHeader().setDefaultSectionSize(103)
        self.table_product_2.verticalHeader().setDefaultSectionSize(30)
        self.btn_buscar_2 = QtWidgets.QPushButton(self.ProductosDadosDeBaja)
        self.btn_buscar_2.setGeometry(QtCore.QRect(390, 130, 75, 21))
        self.btn_buscar_2.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_buscar_2.setObjectName("btn_buscar_2")
        self.btn_darDeAlta = QtWidgets.QPushButton(self.ProductosDadosDeBaja)
        self.btn_darDeAlta.setGeometry(QtCore.QRect(570, 560, 131, 30))
        self.btn_darDeAlta.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_darDeAlta.setFont(font)
        self.btn_darDeAlta.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_darDeAlta.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_darDeAlta.setObjectName("btn_darDeAlta")
        self.btn_limpiar_2 = QtWidgets.QPushButton(self.ProductosDadosDeBaja)
        self.btn_limpiar_2.setGeometry(QtCore.QRect(480, 130, 75, 21))
        self.btn_limpiar_2.setStyleSheet("background-color: rgb(212, 212, 212);")
        self.btn_limpiar_2.setObjectName("btn_limpiar_2")
        self.tabWidget.addTab(self.ProductosDadosDeBaja, "")

        self.retranslateUi(listaDeProductos)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(listaDeProductos)

        #Inputs con validadores
        self.input_codigo.setValidator(intValidator)
        self.input_codigo_2.setValidator(intValidator)

        self.completer_nameProd = QCompleter(self.productos.autoComplete()) 
        self.input_prod.setCompleter(self.completer_nameProd)

        self.completer_nameProd_2 = QCompleter(self.productos.autoComplete_2())
        self.input_prod_2.setCompleter(self.completer_nameProd_2)
        
        

        self.a = self.btn_actualizar.clicked.connect(lambda:self.controlstock_controller.listarProductosActivos())
        self.b = self.btn_create.clicked.connect(lambda:self.controlstock_controller.openCreate(Ui_CreateProduct))
        self.c = self.btn_actualizar_2.clicked.connect(lambda:self.controlstock_controller.listarBajaProductos())
        self.d = self.btn_darDeAlta.clicked.connect(lambda:self.controlstock_controller.darAltaProducto())
        self.e = self.btn_buscar.clicked.connect(lambda:self.controlstock_controller.buscarProductoActivo(self.input_codigo.text(), self.input_prod.text()))
        self.e = self.btn_buscar_2.clicked.connect(lambda:self.controlstock_controller.buscarProductoBaja(self.input_codigo_2.text(), self.input_prod_2.text()))
        self.e = self.btn_limpiar.clicked.connect(lambda:self.controlstock_controller.limpiar())
        self.e = self.btn_limpiar_2.clicked.connect(lambda:self.controlstock_controller.limpiar_2())
        self.p = self.btn_volver.clicked.connect(lambda:self.controlstock_controller.salir(listaDeProductos))
        self.p = self.btn_volver_2.clicked.connect(lambda:self.controlstock_controller.salir(listaDeProductos))
        #--------------------End Events------------------------------

    def retranslateUi(self, listaDeProductos):
        _translate = QtCore.QCoreApplication.translate
        listaDeProductos.setWindowTitle(_translate("listaDeProductos", "Lista de Productos"))
        self.label.setText(_translate("listaDeProductos", "Productos Activos"))
        self.label_2.setText(_translate("listaDeProductos", "Codigo de Barras"))
        self.btn_buscar.setText(_translate("listaDeProductos", "Buscar"))
        item = self.table_product.horizontalHeaderItem(0)
        item.setText(_translate("listaDeProductos", "CódProducto"))
        item = self.table_product.horizontalHeaderItem(1)
        item.setText(_translate("listaDeProductos", "Código de Barras"))
        item = self.table_product.horizontalHeaderItem(2)
        item.setText(_translate("listaDeProductos", "Producto"))
        item = self.table_product.horizontalHeaderItem(3)
        item.setText(_translate("listaDeProductos", "Categoría"))
        item = self.table_product.horizontalHeaderItem(4)
        item.setText(_translate("listaDeProductos", "Subcategoría"))
        item = self.table_product.horizontalHeaderItem(5)
        item.setText(_translate("listaDeProductos", "Marca"))
        item = self.table_product.horizontalHeaderItem(6)
        item.setText(_translate("listaDeProductos", "Tipo Unidad"))
        item = self.table_product.horizontalHeaderItem(7)
        item.setText(_translate("listaDeProductos", "Unidad Medida"))
        item = self.table_product.horizontalHeaderItem(8)
        item.setText(_translate("listaDeProductos", "Cant. en Stock"))
        item = self.table_product.horizontalHeaderItem(9)
        item.setText(_translate("listaDeProductos", "Stock Min."))
        item = self.table_product.horizontalHeaderItem(10)
        item.setText(_translate("listaDeProductos", "Punto de Pedido"))
        item = self.table_product.horizontalHeaderItem(11)
        item.setText(_translate("listaDeProductos", "Costo Compra"))
        item = self.table_product.horizontalHeaderItem(12)
        item.setText(_translate("listaDeProductos", "Precio Venta"))
        self.label_3.setText(_translate("listaDeProductos", "Producto"))
        self.btn_actualizar.setText(_translate("listaDeProductos", "Actualizar"))
        self.btn_create.setText(_translate("listaDeProductos", "Crear"))
        self.btn_volver.setText(_translate("listaDeProductos", "Salir"))
        self.btn_limpiar.setText(_translate("listaDeProductos", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProductosActivos), _translate("listaDeProductos", "Productos Activos"))
        self.btn_volver_2.setText(_translate("listaDeProductos", "Salir"))
        self.label_4.setText(_translate("listaDeProductos", "Codigo de Barras"))
        self.btn_actualizar_2.setText(_translate("listaDeProductos", "Actualizar"))
        self.label_5.setText(_translate("listaDeProductos", "Producto"))
        self.label_6.setText(_translate("listaDeProductos", "Productos dados de baja"))
        item = self.table_product_2.horizontalHeaderItem(0)
        item.setText(_translate("listaDeProductos", "CodProducto"))
        item = self.table_product_2.horizontalHeaderItem(1)
        item.setText(_translate("listaDeProductos", "Código de Barras"))
        item = self.table_product_2.horizontalHeaderItem(2)
        item.setText(_translate("listaDeProductos", "Producto"))
        item = self.table_product_2.horizontalHeaderItem(3)
        item.setText(_translate("listaDeProductos", "Categoría"))
        item = self.table_product_2.horizontalHeaderItem(4)
        item.setText(_translate("listaDeProductos", "Subcategoría"))
        item = self.table_product_2.horizontalHeaderItem(5)
        item.setText(_translate("listaDeProductos", "Marca"))
        item = self.table_product_2.horizontalHeaderItem(6)
        item.setText(_translate("listaDeProductos", "Tipo Unidad"))
        item = self.table_product_2.horizontalHeaderItem(7)
        item.setText(_translate("listaDeProductos", "Unidad de Medida"))
        item = self.table_product_2.horizontalHeaderItem(8)
        item.setText(_translate("listaDeProductos", "Cant. en Stock"))
        item = self.table_product_2.horizontalHeaderItem(9)
        item.setText(_translate("listaDeProductos", "Punto de Pedido"))
        item = self.table_product_2.horizontalHeaderItem(10)
        item.setText(_translate("listaDeProductos", "Costo de Compra"))
        item = self.table_product_2.horizontalHeaderItem(11)
        item.setText(_translate("listaDeProductos", "Precio Venta"))
        self.btn_buscar_2.setText(_translate("listaDeProductos", "Buscar"))
        self.btn_darDeAlta.setText(_translate("listaDeProductos", "Dar de alta"))
        self.btn_limpiar_2.setText(_translate("listaDeProductos", "Limpiar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ProductosDadosDeBaja), _translate("listaDeProductos", "Productos dados de baja"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    listaDeProductos = QtWidgets.QWidget()
    ui = Ui_listaDeProductos()
    ui.setupUi(listaDeProductos)
    listaDeProductos.show()
    sys.exit(app.exec_())