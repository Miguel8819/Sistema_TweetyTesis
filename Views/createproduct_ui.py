
import sys
import os

from pymysql import STRING
myDir = os.getcwd()
sys.path.append(myDir)
from wsgiref.validate import validator
from Controllers.CreateProductController import CreateProductController
from PyQt5 import QtCore, QtGui, QtWidgets
from Models.Product import Product
from Database.Connection import connection
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QDoubleValidator, QValidator

class Ui_CreateProduct(object):
    def __init__(self):
        self.create_product_controller = CreateProductController(self)
        self.product = Product(connection())
    def setupUi(self, CreateProduct):
        #Validador de input en int
        intValidator = QRegExpValidator(QRegExp(r'[0-9\s]+'))
        
        #Validador de input string
        stringValidator = QRegExpValidator(QRegExp(r'[a-zA-Z\s]+'))

        CreateProduct.setObjectName("CreateProduct")
        CreateProduct.resize(899, 700)
        self.btn_create = QtWidgets.QPushButton(CreateProduct)
        self.btn_create.setGeometry(QtCore.QRect(130, 610, 300, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_create.setFont(font)
        self.btn_create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_create.setObjectName("btn_create")
        self.TitAgregarProd = QtWidgets.QLabel(CreateProduct)
        self.TitAgregarProd.setGeometry(QtCore.QRect(30, 10, 300, 33))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.TitAgregarProd.setFont(font)
        self.TitAgregarProd.setObjectName("TitAgregarProd")
        self.btn_exit = QtWidgets.QPushButton(CreateProduct)
        self.btn_exit.setGeometry(QtCore.QRect(300, 660, 300, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setObjectName("btn_exit")
        self.btn_cancel = QtWidgets.QPushButton(CreateProduct)
        self.btn_cancel.setGeometry(QtCore.QRect(460, 610, 300, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setObjectName("btn_cancel")
        self.label_datBasic = QtWidgets.QLabel(CreateProduct)
        self.label_datBasic.setGeometry(QtCore.QRect(20, 60, 131, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_datBasic.setFont(font)
        self.label_datBasic.setObjectName("label_datBasic")
        self.layoutWidget = QtWidgets.QWidget(CreateProduct)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 90, 271, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_codBarra = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_codBarra.setFont(font)
        self.label_codBarra.setObjectName("label_codBarra")
        self.verticalLayout.addWidget(self.label_codBarra)
        self.input_codBarra = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_codBarra.setFont(font)
        self.input_codBarra.setMaxLength(15)
        self.input_codBarra.setAlignment(QtCore.Qt.AlignCenter)
        self.input_codBarra.setObjectName("input_codBarra")
        self.verticalLayout.addWidget(self.input_codBarra)
        self.layoutWidget1 = QtWidgets.QWidget(CreateProduct)
        self.layoutWidget1.setGeometry(QtCore.QRect(400, 90, 451, 51))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_cant = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_cant.setFont(font)
        self.label_cant.setObjectName("label_cant")
        self.verticalLayout_2.addWidget(self.label_cant)
        self.input_prod = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_prod.setFont(font)
        self.input_prod.setText("")
        self.input_prod.setMaxLength(40)
        self.input_prod.setAlignment(QtCore.Qt.AlignCenter)
        self.input_prod.setObjectName("input_prod")
        self.verticalLayout_2.addWidget(self.input_prod)
        self.layoutWidget2 = QtWidgets.QWidget(CreateProduct)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 170, 141, 61))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_descrip = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_descrip.setFont(font)
        self.label_descrip.setObjectName("label_descrip")
        self.verticalLayout_3.addWidget(self.label_descrip)
        self.box_cat = QtWidgets.QComboBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.box_cat.setFont(font)
        self.box_cat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.box_cat.setObjectName("box_cat")
        self.box_cat.addItem("")
        self.box_cat.addItem("")
        self.box_cat.addItem("")
        self.box_cat.addItem("")
        self.box_cat.addItem("")
        self.box_cat.addItem("")
        self.box_cat.setItemText(5, "")
        self.verticalLayout_3.addWidget(self.box_cat)
        self.layoutWidget3 = QtWidgets.QWidget(CreateProduct)
        self.layoutWidget3.setGeometry(QtCore.QRect(220, 170, 141, 61))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_categoria = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_categoria.setFont(font)
        self.label_categoria.setObjectName("label_categoria")
        self.verticalLayout_4.addWidget(self.label_categoria)
        self.box_subCat = QtWidgets.QComboBox(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.box_subCat.setFont(font)
        self.box_subCat.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.box_subCat.setObjectName("box_subCat")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.box_subCat.addItem("")
        self.verticalLayout_4.addWidget(self.box_subCat)
        self.layoutWidget4 = QtWidgets.QWidget(CreateProduct)
        self.layoutWidget4.setGeometry(QtCore.QRect(400, 170, 281, 61))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_precio = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_precio.setFont(font)
        self.label_precio.setObjectName("label_precio")
        self.verticalLayout_5.addWidget(self.label_precio)
        self.box_marca = QtWidgets.QComboBox(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.box_marca.setFont(font)
        self.box_marca.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.box_marca.setObjectName("box_marca")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.box_marca.addItem("")
        self.verticalLayout_5.addWidget(self.box_marca)
        self.frame = QtWidgets.QFrame(CreateProduct)
        self.frame.setGeometry(QtCore.QRect(10, 480, 881, 111))
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.label_datCompraVenta = QtWidgets.QLabel(self.frame)
        self.label_datCompraVenta.setGeometry(QtCore.QRect(10, 10, 211, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_datCompraVenta.setFont(font)
        self.label_datCompraVenta.setObjectName("label_datCompraVenta")
        self.layoutWidget5 = QtWidgets.QWidget(self.frame)
        self.layoutWidget5.setGeometry(QtCore.QRect(430, 40, 301, 51))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_precVenta = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_precVenta.setFont(font)
        self.label_precVenta.setObjectName("label_precVenta")
        self.verticalLayout_12.addWidget(self.label_precVenta)
        self.input_precVenta = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_precVenta.setFont(font)
        self.input_precVenta.setMaxLength(9)
        self.input_precVenta.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_precVenta.setObjectName("input_precVenta")
        self.verticalLayout_12.addWidget(self.input_precVenta)
        self.layoutWidget6 = QtWidgets.QWidget(self.frame)
        self.layoutWidget6.setGeometry(QtCore.QRect(40, 40, 301, 51))
        self.layoutWidget6.setObjectName("layoutWidget6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_costCompr = QtWidgets.QLabel(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_costCompr.setFont(font)
        self.label_costCompr.setObjectName("label_costCompr")
        self.verticalLayout_11.addWidget(self.label_costCompr)
        self.input_costCompra = QtWidgets.QLineEdit(self.layoutWidget6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_costCompra.setFont(font)
        self.input_costCompra.setMaxLength(8)
        self.input_costCompra.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.input_costCompra.setObjectName("input_costCompra")
        self.verticalLayout_11.addWidget(self.input_costCompra)
        self.frame_2 = QtWidgets.QFrame(CreateProduct)
        self.frame_2.setGeometry(QtCore.QRect(10, 260, 881, 201))
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.frame_2.setObjectName("frame_2")
        self.label_datStock = QtWidgets.QLabel(self.frame_2)
        self.label_datStock.setGeometry(QtCore.QRect(10, 10, 131, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_datStock.setFont(font)
        self.label_datStock.setObjectName("label_datStock")
        self.layoutWidget7 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget7.setGeometry(QtCore.QRect(210, 40, 181, 61))
        self.layoutWidget7.setObjectName("layoutWidget7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_uniMed = QtWidgets.QLabel(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_uniMed.setFont(font)
        self.label_uniMed.setObjectName("label_uniMed")
        self.verticalLayout_7.addWidget(self.label_uniMed)
        self.box_uniMedi = QtWidgets.QComboBox(self.layoutWidget7)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.box_uniMedi.setFont(font)
        self.box_uniMedi.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.box_uniMedi.setObjectName("box_uniMedi")
        self.box_uniMedi.addItem("")
        self.verticalLayout_7.addWidget(self.box_uniMedi)
        self.layoutWidget8 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget8.setGeometry(QtCore.QRect(40, 40, 141, 61))
        self.layoutWidget8.setObjectName("layoutWidget8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_tipoUni = QtWidgets.QLabel(self.layoutWidget8)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_tipoUni.setFont(font)
        self.label_tipoUni.setObjectName("label_tipoUni")
        self.verticalLayout_6.addWidget(self.label_tipoUni)
        self.box_tipoUnid = QtWidgets.QComboBox(self.layoutWidget8)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.box_tipoUnid.setFont(font)
        self.box_tipoUnid.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.box_tipoUnid.setObjectName("box_tipoUnid")
        self.box_tipoUnid.addItem("")
        self.verticalLayout_6.addWidget(self.box_tipoUnid)
        self.layoutWidget9 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget9.setGeometry(QtCore.QRect(430, 130, 301, 51))
        self.layoutWidget9.setObjectName("layoutWidget9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_puntPedi = QtWidgets.QLabel(self.layoutWidget9)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_puntPedi.setFont(font)
        self.label_puntPedi.setObjectName("label_puntPedi")
        self.verticalLayout_10.addWidget(self.label_puntPedi)
        self.input_puntoPedido = QtWidgets.QLineEdit(self.layoutWidget9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_puntoPedido.setFont(font)
        self.input_puntoPedido.setMaxLength(5)
        self.input_puntoPedido.setAlignment(QtCore.Qt.AlignCenter)
        self.input_puntoPedido.setObjectName("input_puntoPedido")
        self.verticalLayout_10.addWidget(self.input_puntoPedido)
        self.layoutWidget10 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget10.setGeometry(QtCore.QRect(40, 130, 301, 51))
        self.layoutWidget10.setObjectName("layoutWidget10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_cantMinStock = QtWidgets.QLabel(self.layoutWidget10)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_cantMinStock.setFont(font)
        self.label_cantMinStock.setObjectName("label_cantMinStock")
        self.verticalLayout_9.addWidget(self.label_cantMinStock)
        self.input_cantMinStock = QtWidgets.QLineEdit(self.layoutWidget10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_cantMinStock.setFont(font)
        self.input_cantMinStock.setMaxLength(5)
        self.input_cantMinStock.setAlignment(QtCore.Qt.AlignCenter)
        self.input_cantMinStock.setObjectName("input_cantMinStock")
        self.verticalLayout_9.addWidget(self.input_cantMinStock)
        self.label = QtWidgets.QLabel(CreateProduct)
        self.label.setGeometry(QtCore.QRect(670, 30, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color: rgb(255, 0, 0)}")
        self.label.setObjectName("label")
        self.frame_2.raise_()
        self.frame.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.btn_create.raise_()
        self.btn_exit.raise_()
        self.btn_cancel.raise_()
        self.label.raise_()
        self.label_datBasic.raise_()
        self.TitAgregarProd.raise_()

        self.retranslateUi(CreateProduct)
        QtCore.QMetaObject.connectSlotsByName(CreateProduct)
        CreateProduct.setTabOrder(self.input_prod, self.box_cat)
        CreateProduct.setTabOrder(self.box_cat, self.box_subCat)
        CreateProduct.setTabOrder(self.box_subCat, self.box_marca)
        CreateProduct.setTabOrder(self.box_marca, self.box_tipoUnid)
        CreateProduct.setTabOrder(self.box_tipoUnid, self.box_uniMedi)
        CreateProduct.setTabOrder(self.box_uniMedi, self.input_cantMinStock)
        CreateProduct.setTabOrder(self.input_cantMinStock, self.input_puntoPedido)
        CreateProduct.setTabOrder(self.input_puntoPedido, self.input_costCompra)
        CreateProduct.setTabOrder(self.input_costCompra, self.input_precVenta)
        CreateProduct.setTabOrder(self.input_precVenta, self.btn_create)
        CreateProduct.setTabOrder(self.btn_create, self.btn_cancel)
        CreateProduct.setTabOrder(self.btn_cancel, self.btn_exit)

         #Inputs con validadores
        self.input_codBarra.setValidator(intValidator)
        self.input_cantMinStock.setValidator(intValidator)
        self.input_puntoPedido.setValidator(intValidator)
        self.input_costCompra.setValidator(intValidator)
        self.input_precVenta.setValidator(intValidator)

       
        

        #--------------------Events--------------------------------------
        self.x = self.btn_create.clicked.connect(lambda:self.create_product_controller.createProduct(self.input_codBarra.text(),self.input_prod.text(), self.box_cat.currentText(),self.box_subCat.currentText(),self.box_marca.currentText(),self.box_tipoUnid.currentText(),self.box_uniMedi.currentText(),self.input_cantMinStock.text(),self.input_puntoPedido.text(),self.input_costCompra.text(),self.input_precVenta.text(), CreateProduct))
        
        self.c = self.btn_cancel.clicked.connect(lambda:self.create_product_controller.borrar())
        self.e = self.btn_exit.clicked.connect(lambda:self.create_product_controller.salir(CreateProduct))
        #--------------------End Events---------------------------------

    def retranslateUi(self, CreateProduct):
        _translate = QtCore.QCoreApplication.translate
        CreateProduct.setWindowTitle(_translate("CreateProduct", "Agregar Producto"))
        self.btn_create.setText(_translate("CreateProduct", "Crear"))
        self.TitAgregarProd.setText(_translate("CreateProduct", "Agregar Producto"))
        self.btn_exit.setText(_translate("CreateProduct", "Salir"))
        self.btn_cancel.setText(_translate("CreateProduct", "Cancelar"))
        self.label_datBasic.setText(_translate("CreateProduct", "- Datos Basicos"))
        self.label_codBarra.setText(_translate("CreateProduct", "Código Barra:"))
        self.input_codBarra.setPlaceholderText(_translate("CreateProduct", "Cód. Barra"))
        self.label_cant.setText(_translate("CreateProduct", "<html><head/><body><p>Producto<span style=\" font-weight:400;\">(*)</span>:</p></body></html>"))
        self.input_prod.setPlaceholderText(_translate("CreateProduct", "Producto"))
        self.label_descrip.setText(_translate("CreateProduct", "Categoria:"))
        self.box_cat.setItemText(0, _translate("CreateProduct", "Articulos escolares"))
        self.box_cat.setItemText(1, _translate("CreateProduct", "Utiles"))
        self.box_cat.setItemText(2, _translate("CreateProduct", "Papeleria"))
        self.box_cat.setItemText(3, _translate("CreateProduct", "Artística"))
        self.box_cat.setItemText(4, _translate("CreateProduct", "Otro"))
        self.label_categoria.setText(_translate("CreateProduct", "Sub Categoría:"))
        self.box_subCat.setItemText(0, _translate("CreateProduct", "Lapiceras"))
        self.box_subCat.setItemText(1, _translate("CreateProduct", "Block hojas"))
        self.box_subCat.setItemText(2, _translate("CreateProduct", "Acuarelas"))
        self.box_subCat.setItemText(3, _translate("CreateProduct", "Carpetas"))
        self.box_subCat.setItemText(4, _translate("CreateProduct", "Pinceles"))
        self.box_subCat.setItemText(5, _translate("CreateProduct", "Temperas"))
        self.box_subCat.setItemText(6, _translate("CreateProduct", "Acrilicos"))
        self.box_subCat.setItemText(7, _translate("CreateProduct", "Plasticola"))
        self.box_subCat.setItemText(8, _translate("CreateProduct", "Cinta adhesiva"))
        self.box_subCat.setItemText(9, _translate("CreateProduct", "Repuestos hojas"))
        self.box_subCat.setItemText(10, _translate("CreateProduct", "Cuadernos"))
        self.box_subCat.setItemText(11, _translate("CreateProduct", "Lapices"))
        self.box_subCat.setItemText(12, _translate("CreateProduct", "Crayones"))
        self.box_subCat.setItemText(13, _translate("CreateProduct", "Fibras"))
        self.box_subCat.setItemText(14, _translate("CreateProduct", "Fibrones"))
        self.box_subCat.setItemText(15, _translate("CreateProduct", "Alfileres"))
        self.box_subCat.setItemText(16, _translate("CreateProduct", "Barniz"))
        self.box_subCat.setItemText(17, _translate("CreateProduct", "Broches"))
        self.box_subCat.setItemText(18, _translate("CreateProduct", "Canopla"))
        self.box_subCat.setItemText(19, _translate("CreateProduct", "Cartuchera"))
        self.box_subCat.setItemText(20, _translate("CreateProduct", "Corrector"))
        self.box_subCat.setItemText(21, _translate("CreateProduct", "Escuadra"))
        self.box_subCat.setItemText(22, _translate("CreateProduct", "Folios"))
        self.box_subCat.setItemText(23, _translate("CreateProduct", "Portaminas"))
        self.box_subCat.setItemText(24, _translate("CreateProduct", "Libreta"))
        self.box_subCat.setItemText(25, _translate("CreateProduct", "Fibron marcador"))
        self.box_subCat.setItemText(26, _translate("CreateProduct", "Resaltador"))
        self.box_subCat.setItemText(27, _translate("CreateProduct", "Otros"))
        self.label_precio.setText(_translate("CreateProduct", "Marca:"))
        self.box_marca.setItemText(0, _translate("CreateProduct", "Bic"))
        self.box_marca.setItemText(1, _translate("CreateProduct", "Maped"))
        self.box_marca.setItemText(2, _translate("CreateProduct", "Sabonis"))
        self.box_marca.setItemText(3, _translate("CreateProduct", "Trabi"))
        self.box_marca.setItemText(4, _translate("CreateProduct", "Faber Castell"))
        self.box_marca.setItemText(5, _translate("CreateProduct", "Pizzini"))
        self.box_marca.setItemText(6, _translate("CreateProduct", "Rivadavia"))
        self.box_marca.setItemText(7, _translate("CreateProduct", "Gloria"))
        self.box_marca.setItemText(8, _translate("CreateProduct", "Laprida"))
        self.box_marca.setItemText(9, _translate("CreateProduct", "Exito"))
        self.box_marca.setItemText(10, _translate("CreateProduct", "2020"))
        self.box_marca.setItemText(11, _translate("CreateProduct", "1810"))
        self.box_marca.setItemText(12, _translate("CreateProduct", "Eterna"))
        self.box_marca.setItemText(13, _translate("CreateProduct", "Luma"))
        self.box_marca.setItemText(14, _translate("CreateProduct", "Nor-Pac"))
        self.box_marca.setItemText(15, _translate("CreateProduct", "Triunfante"))
        self.box_marca.setItemText(16, _translate("CreateProduct", "Edding"))
        self.box_marca.setItemText(17, _translate("CreateProduct", "Sharpie"))
        self.box_marca.setItemText(18, _translate("CreateProduct", "Boreal"))
        self.box_marca.setItemText(19, _translate("CreateProduct", "Pampa"))
        self.box_marca.setItemText(20, _translate("CreateProduct", "Otro"))
        self.label_datCompraVenta.setText(_translate("CreateProduct", "- Datos Compra/Venta"))
        self.label_precVenta.setText(_translate("CreateProduct", "<html><head/><body><p>Precio de Venta<span style=\" font-weight:400;\">(*)</span>:</p></body></html>"))
        self.input_precVenta.setPlaceholderText(_translate("CreateProduct", "$0.00"))
        self.label_costCompr.setText(_translate("CreateProduct", "<html><head/><body><p>Costo de Compra<span style=\" font-weight:400;\">(*)</span>:</p></body></html>"))
        self.input_costCompra.setPlaceholderText(_translate("CreateProduct", "$0.00"))
        self.label_datStock.setText(_translate("CreateProduct", "- Datos Stock"))
        self.label_uniMed.setText(_translate("CreateProduct", "<html><head/><body><p>Unidad de Medida<span style=\" font-weight:400;\">(*)</span>:</p></body></html>"))
        self.box_uniMedi.setItemText(0, _translate("CreateProduct", "Unidad"))
        self.label_tipoUni.setText(_translate("CreateProduct", "<html><head/><body><p>Tipo Unidad<span style=\" font-weight:400;\">(*)</span>:</p></body></html>"))
        self.box_tipoUnid.setItemText(0, _translate("CreateProduct", "Unidad"))
        self.label_puntPedi.setText(_translate("CreateProduct", "<html><head/><body><p>Punto de Pedido<span style=\" font-weight:400;\">(*)</span>:</p></body></html>"))
        self.input_puntoPedido.setPlaceholderText(_translate("CreateProduct", "Punto de Pedido"))
        self.label_cantMinStock.setText(_translate("CreateProduct", "<html><head/><body><p>Cantidad Minima Stock<span style=\" font-weight:400;\">(*)</span>:</p></body></html>"))
        self.input_cantMinStock.setPlaceholderText(_translate("CreateProduct", "Cant. Min. Stock"))
        self.label.setText(_translate("CreateProduct", "Los campos con (*) son obligatorios"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateProduct = QtWidgets.QWidget()
    ui = Ui_CreateProduct()
    ui.setupUi(CreateProduct)
    CreateProduct.show()
    sys.exit(app.exec_())
