# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuprincipal.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.menuprincipalController import menuprincipalController
from venta_ui import Ui_venta
from controlstock_ui import Ui_controlstock
from proveedores_ui import Ui_proveedores
from createproduct_ui import Ui_CreateProduct
from cliente_ui import Ui_clientes


class Ui_menuprincipal(object):
    def __init__(self):
        self.menuprincipalController = menuprincipalController(self)
    def setupUi(self, menuprincipal):
        menuprincipal.setObjectName("menuprincipal")
        menuprincipal.resize(795, 600)
        menuprincipal.setStyleSheet("")
        self.frame = QtWidgets.QFrame(menuprincipal)
        self.frame.setGeometry(QtCore.QRect(9, 9, 231, 582))
        self.frame.setStyleSheet("QFrame{background-color:rgb(51,102,255)}\n"
"QPushButton{background-color:rgb(61,61,61);border-top-left-radius: 20px; border-bottom-left-radius: 20px;color: rgb(255,255,255);}\n"
"QPushButton:hover{background-color:white; border-top-left-radius: 20px;border-bottom-left-radius: 20px;color: rgb(0,0,0);}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(40, 510, 191, 61))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(0, 490, 71, 91))
        self.label_7.setMinimumSize(QtCore.QSize(45, 45))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Imagenes/pngfind.com-bird-png-600629.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.btn_mantenimiento = QtWidgets.QPushButton(self.frame)
        self.btn_mantenimiento.setGeometry(QtCore.QRect(11, 422, 209, 50))
        self.btn_mantenimiento.setMinimumSize(QtCore.QSize(209, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mantenimiento.setFont(font)
        self.btn_mantenimiento.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/mantenimiento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_mantenimiento.setIcon(icon)
        self.btn_mantenimiento.setIconSize(QtCore.QSize(35, 35))
        self.btn_mantenimiento.setObjectName("btn_mantenimiento")
        self.btn_gestionCompra = QtWidgets.QPushButton(self.frame)
        self.btn_gestionCompra.setGeometry(QtCore.QRect(11, 102, 209, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_gestionCompra.sizePolicy().hasHeightForWidth())
        self.btn_gestionCompra.setSizePolicy(sizePolicy)
        self.btn_gestionCompra.setMinimumSize(QtCore.QSize(209, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_gestionCompra.setFont(font)
        self.btn_gestionCompra.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagenes/comprar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_gestionCompra.setIcon(icon1)
        self.btn_gestionCompra.setIconSize(QtCore.QSize(35, 35))
        self.btn_gestionCompra.setAutoDefault(False)
        self.btn_gestionCompra.setObjectName("btn_gestionCompra")
        self.btn_gestionVenta = QtWidgets.QPushButton(self.frame)
        self.btn_gestionVenta.setGeometry(QtCore.QRect(11, 182, 209, 50))
        self.btn_gestionVenta.setMinimumSize(QtCore.QSize(209, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_gestionVenta.setFont(font)
        self.btn_gestionVenta.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Imagenes/punto-de-venta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_gestionVenta.setIcon(icon2)
        self.btn_gestionVenta.setIconSize(QtCore.QSize(35, 35))
        self.btn_gestionVenta.setObjectName("btn_gestionVenta")
        self.btn_gestionStock = QtWidgets.QPushButton(self.frame)
        self.btn_gestionStock.setGeometry(QtCore.QRect(11, 262, 209, 50))
        self.btn_gestionStock.setMinimumSize(QtCore.QSize(209, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_gestionStock.setFont(font)
        self.btn_gestionStock.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Imagenes/en-stock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_gestionStock.setIcon(icon3)
        self.btn_gestionStock.setIconSize(QtCore.QSize(35, 35))
        self.btn_gestionStock.setObjectName("btn_gestionStock")
        self.btn_administracion = QtWidgets.QPushButton(self.frame)
        self.btn_administracion.setGeometry(QtCore.QRect(11, 342, 209, 50))
        self.btn_administracion.setMinimumSize(QtCore.QSize(209, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_administracion.setFont(font)
        self.btn_administracion.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("Imagenes/investigacion.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_administracion.setIcon(icon4)
        self.btn_administracion.setIconSize(QtCore.QSize(35, 35))
        self.btn_administracion.setObjectName("btn_administracion")
        self.frame_2 = QtWidgets.QFrame(menuprincipal)
        self.frame_2.setGeometry(QtCore.QRect(250, 9, 541, 582))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_gestionCompra = QtWidgets.QWidget()
        self.page_gestionCompra.setStyleSheet("QWidget{background-color:rgb(153,204,255)}\n"
"QPushButton{background-color: rgb(61,61,61); border-top-right-radius: 20px; border-bottom-right-radius: 20px;color: rgb(255,255,255);}\n"
"QPushButton:hover{background-color:white; border-top-right-radius: 20px;border-bottom-right-radius: 20px;color: rgb(0,0,0);}\n"
"\n"
"\n"
"")
        self.page_gestionCompra.setObjectName("page_gestionCompra")
        self.label = QtWidgets.QLabel(self.page_gestionCompra)
        self.label.setGeometry(QtCore.QRect(120, 20, 290, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btn_proveedores = QtWidgets.QPushButton(self.page_gestionCompra)
        self.btn_proveedores.setGeometry(QtCore.QRect(131, 102, 290, 50))
        self.btn_proveedores.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_proveedores.setFont(font)
        self.btn_proveedores.setObjectName("btn_proveedores")
        self.label_8 = QtWidgets.QLabel(self.page_gestionCompra)
        self.label_8.setGeometry(QtCore.QRect(380, 30, 45, 45))
        self.label_8.setMinimumSize(QtCore.QSize(45, 45))
        self.label_8.setMaximumSize(QtCore.QSize(45, 45))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("Imagenes/comprar.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.btn_genOrdenCompra = QtWidgets.QPushButton(self.page_gestionCompra)
        self.btn_genOrdenCompra.setGeometry(QtCore.QRect(131, 182, 290, 50))
        self.btn_genOrdenCompra.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_genOrdenCompra.setFont(font)
        self.btn_genOrdenCompra.setObjectName("btn_genOrdenCompra")
        self.stackedWidget.addWidget(self.page_gestionCompra)
        self.page_gestionVenta = QtWidgets.QWidget()
        self.page_gestionVenta.setStyleSheet("QWidget{background-color:rgb(153,204,255)}\n"
"QPushButton{background-color: rgb(61,61,61); border-top-right-radius: 20px; border-bottom-right-radius: 20px;color: rgb(255,255,255);}\n"
"QPushButton:hover{background-color:white; border-top-right-radius: 20px;border-bottom-right-radius: 20px;color: rgb(0,0,0);}")
        self.page_gestionVenta.setObjectName("page_gestionVenta")
        self.label_2 = QtWidgets.QLabel(self.page_gestionVenta)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 290, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.page_gestionVenta)
        self.label_9.setGeometry(QtCore.QRect(380, 30, 45, 45))
        self.label_9.setMinimumSize(QtCore.QSize(45, 45))
        self.label_9.setMaximumSize(QtCore.QSize(45, 45))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("Imagenes/punto-de-venta.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.btn_infDeVentas = QtWidgets.QPushButton(self.page_gestionVenta)
        self.btn_infDeVentas.setGeometry(QtCore.QRect(131, 182, 290, 50))
        self.btn_infDeVentas.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_infDeVentas.setFont(font)
        self.btn_infDeVentas.setObjectName("btn_infDeVentas")
        self.btn_facturacion = QtWidgets.QPushButton(self.page_gestionVenta)
        self.btn_facturacion.setGeometry(QtCore.QRect(131, 102, 290, 50))
        self.btn_facturacion.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_facturacion.setFont(font)
        self.btn_facturacion.setObjectName("btn_facturacion")
        self.btn_dbClientes = QtWidgets.QPushButton(self.page_gestionVenta)
        self.btn_dbClientes.setGeometry(QtCore.QRect(131, 262, 290, 50))
        self.btn_dbClientes.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dbClientes.setFont(font)
        self.btn_dbClientes.setObjectName("btn_dbClientes")
        self.stackedWidget.addWidget(self.page_gestionVenta)
        self.page_gestionStock = QtWidgets.QWidget()
        self.page_gestionStock.setStyleSheet("QWidget{background-color:rgb(153,204,255)}\n"
"QPushButton{background-color: rgb(61,61,61); border-top-right-radius: 20px; border-bottom-right-radius: 20px;color: rgb(255,255,255);}\n"
"QPushButton:hover{background-color:white; border-top-right-radius: 20px;border-bottom-right-radius: 20px;color: rgb(0,0,0);}\n"
"")
        self.page_gestionStock.setObjectName("page_gestionStock")
        self.label_3 = QtWidgets.QLabel(self.page_gestionStock)
        self.label_3.setGeometry(QtCore.QRect(120, 20, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.btn_controlStock = QtWidgets.QPushButton(self.page_gestionStock)
        self.btn_controlStock.setGeometry(QtCore.QRect(131, 102, 290, 50))
        self.btn_controlStock.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_controlStock.setFont(font)
        self.btn_controlStock.setObjectName("btn_controlStock")
        self.label_5 = QtWidgets.QLabel(self.page_gestionStock)
        self.label_5.setGeometry(QtCore.QRect(380, 30, 45, 45))
        self.label_5.setMinimumSize(QtCore.QSize(45, 45))
        self.label_5.setMaximumSize(QtCore.QSize(45, 45))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Imagenes/en-stock.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.btn_abmProd = QtWidgets.QPushButton(self.page_gestionStock)
        self.btn_abmProd.setGeometry(QtCore.QRect(131, 182, 290, 50))
        self.btn_abmProd.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abmProd.setFont(font)
        self.btn_abmProd.setObjectName("btn_abmProd")
        self.btn_movStock = QtWidgets.QPushButton(self.page_gestionStock)
        self.btn_movStock.setGeometry(QtCore.QRect(131, 262, 290, 50))
        self.btn_movStock.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_movStock.setFont(font)
        self.btn_movStock.setObjectName("btn_movStock")
        self.stackedWidget.addWidget(self.page_gestionStock)
        self.page_administracion = QtWidgets.QWidget()
        self.page_administracion.setStyleSheet("QWidget{background-color:rgb(153,204,255)}\n"
"QPushButton{background-color: rgb(61,61,61); border-top-right-radius: 20px; border-bottom-right-radius: 20px;color: rgb(255,255,255);}\n"
"QPushButton:hover{background-color:white; border-top-right-radius: 20px;border-bottom-right-radius: 20px;color: rgb(0,0,0);}")
        self.page_administracion.setObjectName("page_administracion")
        self.label_4 = QtWidgets.QLabel(self.page_administracion)
        self.label_4.setGeometry(QtCore.QRect(120, 20, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.page_administracion)
        self.label_10.setGeometry(QtCore.QRect(380, 30, 45, 45))
        self.label_10.setMinimumSize(QtCore.QSize(45, 45))
        self.label_10.setMaximumSize(QtCore.QSize(45, 45))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("Imagenes/investigacion.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.btn_infDeCaja = QtWidgets.QPushButton(self.page_administracion)
        self.btn_infDeCaja.setGeometry(QtCore.QRect(131, 262, 290, 50))
        self.btn_infDeCaja.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_infDeCaja.setFont(font)
        self.btn_infDeCaja.setObjectName("btn_infDeCaja")
        self.btn_movFondos = QtWidgets.QPushButton(self.page_administracion)
        self.btn_movFondos.setGeometry(QtCore.QRect(131, 102, 290, 50))
        self.btn_movFondos.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_movFondos.setFont(font)
        self.btn_movFondos.setObjectName("btn_movFondos")
        self.btn_abrirCerrarCaja = QtWidgets.QPushButton(self.page_administracion)
        self.btn_abrirCerrarCaja.setGeometry(QtCore.QRect(131, 182, 290, 50))
        self.btn_abrirCerrarCaja.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abrirCerrarCaja.setFont(font)
        self.btn_abrirCerrarCaja.setObjectName("btn_abrirCerrarCaja")
        self.stackedWidget.addWidget(self.page_administracion)
        self.page_mantenimiento = QtWidgets.QWidget()
        self.page_mantenimiento.setStyleSheet("QWidget{background-color:rgb(153,204,255)}\n"
"QPushButton{background-color: rgb(61,61,61); border-top-right-radius: 20px; border-bottom-right-radius: 20px;color: rgb(255,255,255);}\n"
"QPushButton:hover{background-color:white; border-top-right-radius: 20px;border-bottom-right-radius: 20px;color: rgb(0,0,0);}")
        self.page_mantenimiento.setObjectName("page_mantenimiento")
        self.label_11 = QtWidgets.QLabel(self.page_mantenimiento)
        self.label_11.setGeometry(QtCore.QRect(380, 30, 45, 45))
        self.label_11.setMinimumSize(QtCore.QSize(45, 45))
        self.label_11.setMaximumSize(QtCore.QSize(45, 45))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("Imagenes/mantenimiento.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.page_mantenimiento)
        self.label_12.setGeometry(QtCore.QRect(120, 20, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.btn_movFondos_2 = QtWidgets.QPushButton(self.page_mantenimiento)
        self.btn_movFondos_2.setGeometry(QtCore.QRect(131, 102, 290, 50))
        self.btn_movFondos_2.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_movFondos_2.setFont(font)
        self.btn_movFondos_2.setObjectName("btn_movFondos_2")
        self.btn_infDeCaja_2 = QtWidgets.QPushButton(self.page_mantenimiento)
        self.btn_infDeCaja_2.setGeometry(QtCore.QRect(131, 262, 290, 50))
        self.btn_infDeCaja_2.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_infDeCaja_2.setFont(font)
        self.btn_infDeCaja_2.setObjectName("btn_infDeCaja_2")
        self.btn_abrirCerrarCaja_2 = QtWidgets.QPushButton(self.page_mantenimiento)
        self.btn_abrirCerrarCaja_2.setGeometry(QtCore.QRect(131, 182, 290, 50))
        self.btn_abrirCerrarCaja_2.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abrirCerrarCaja_2.setFont(font)
        self.btn_abrirCerrarCaja_2.setObjectName("btn_abrirCerrarCaja_2")
        self.label_12.raise_()
        self.label_11.raise_()
        self.btn_movFondos_2.raise_()
        self.btn_infDeCaja_2.raise_()
        self.btn_abrirCerrarCaja_2.raise_()
        self.stackedWidget.addWidget(self.page_mantenimiento)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(menuprincipal)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(menuprincipal)

#--------------------Events--------------------------------------
        self.btn_gestionCompra.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_gestionCompra))
        self.btn_gestionVenta.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_gestionVenta))
        self.btn_gestionStock.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_gestionStock))
        self.btn_administracion.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_administracion))
        self.btn_mantenimiento.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_mantenimiento))
        self.btn_proveedores.clicked.connect(lambda:self.menuprincipalController.openProveedores(Ui_proveedores, menuprincipal))
        self.btn_controlStock.clicked.connect(lambda:self.menuprincipalController.openControlStock(Ui_controlstock, menuprincipal))
        self.btn_facturacion.clicked.connect(lambda:self.menuprincipalController.openFacturacion(Ui_venta, menuprincipal))
        self.btn_abmProd.clicked.connect(lambda:self.menuprincipalController.openCreateProduct(Ui_CreateProduct, menuprincipal))
        self.btn_dbClientes.clicked.connect(lambda:self.menuprincipalController.openClientes(Ui_clientes, menuprincipal))
#--------------------End Events---------------------------------

    def retranslateUi(self, menuprincipal):
        _translate = QtCore.QCoreApplication.translate
        menuprincipal.setWindowTitle(_translate("menuprincipal", "Menú Principal"))
        self.label_6.setText(_translate("menuprincipal", "Sistema Tweety"))
        self.btn_mantenimiento.setText(_translate("menuprincipal", "Mantenimiento"))
        self.btn_gestionCompra.setText(_translate("menuprincipal", "Gestión de Compra"))
        self.btn_gestionVenta.setText(_translate("menuprincipal", "Gestión de Venta"))
        self.btn_gestionStock.setText(_translate("menuprincipal", "Gestión de Stock"))
        self.btn_administracion.setText(_translate("menuprincipal", "Administración"))
        self.label.setText(_translate("menuprincipal", "Gestión de Compra"))
        self.btn_proveedores.setText(_translate("menuprincipal", "Proveedores"))
        self.btn_genOrdenCompra.setText(_translate("menuprincipal", "Generar Orden de Compra"))
        self.label_2.setText(_translate("menuprincipal", "Gestión de Venta"))
        self.btn_infDeVentas.setText(_translate("menuprincipal", "Informe de Ventas"))
        self.btn_facturacion.setText(_translate("menuprincipal", "Facturación"))
        self.btn_dbClientes.setText(_translate("menuprincipal", "Clientes"))
        self.label_3.setText(_translate("menuprincipal", "Gestión de Stock"))
        self.btn_controlStock.setText(_translate("menuprincipal", "Control de Stock"))
        self.btn_abmProd.setText(_translate("menuprincipal", "ABM Productos"))
        self.btn_movStock.setText(_translate("menuprincipal", "Movimiento de Stock"))
        self.label_4.setText(_translate("menuprincipal", "Administración"))
        self.btn_infDeCaja.setText(_translate("menuprincipal", "Informe de Caja"))
        self.btn_movFondos.setText(_translate("menuprincipal", "Movimientos de Fondos"))
        self.btn_abrirCerrarCaja.setText(_translate("menuprincipal", "Abrir y Cerrar Caja"))
        self.label_12.setText(_translate("menuprincipal", "Mantenimiento"))
        self.btn_movFondos_2.setText(_translate("menuprincipal", "Gestion de Clave"))
        self.btn_infDeCaja_2.setText(_translate("menuprincipal", "Configuración de Usuarios"))
        self.btn_abrirCerrarCaja_2.setText(_translate("menuprincipal", "Gestion de Backup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menuprincipal = QtWidgets.QWidget()
    ui = Ui_menuprincipal()
    ui.setupUi(menuprincipal)
    menuprincipal.show()
    sys.exit(app.exec_())
