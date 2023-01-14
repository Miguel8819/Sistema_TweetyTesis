import sys
import os
from wsgiref.validate import validator

from pymysql import STRING
myDir = os.getcwd()
sys.path.append(myDir)

from Controllers.informeVentasController import listarVentas
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QVBoxLayout
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator, QDoubleValidator, QValidator
from Models.venta import Venta

from PyQt5 import QtCore, QtGui, QtWidgets
from Database.Connection import connection

class Ui_informeDeVentas(object):
    def __init__(self):
        self.listarVentas = listarVentas(self)
        self.cliente = Venta(connection())
    def setupUi(self, informeDeVentas):
        informeDeVentas.setObjectName("informeDeVentas")
        informeDeVentas.resize(950, 637)
        informeDeVentas.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.tabWidget = QtWidgets.QTabWidget(informeDeVentas)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 941, 621))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(350, 140, 211, 341))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.Btn_Volver = QtWidgets.QPushButton(self.tab)
        self.Btn_Volver.setGeometry(QtCore.QRect(560, 490, 75, 23))
        self.Btn_Volver.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_Volver.setObjectName("Btn_Volver")
        self.Btn_Ver_Importes = QtWidgets.QPushButton(self.tab)
        self.Btn_Ver_Importes.setGeometry(QtCore.QRect(270, 140, 75, 23))
        self.Btn_Ver_Importes.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_Ver_Importes.setObjectName("Btn_Ver_Importes")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(310, 10, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.input_fecha_diaria = QtWidgets.QLineEdit(self.tab)
        self.input_fecha_diaria.setGeometry(QtCore.QRect(350, 90, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_fecha_diaria.setFont(font)
        self.input_fecha_diaria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_fecha_diaria.setMaxLength(10)
        self.input_fecha_diaria.setObjectName("input_fecha_diaria")
        self.btn_fecha_diaria = QtWidgets.QPushButton(self.tab)
        self.btn_fecha_diaria.setGeometry(QtCore.QRect(450, 90, 31, 21))
        self.btn_fecha_diaria.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"")
        self.btn_fecha_diaria.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Imagenes/vector-find-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_fecha_diaria.setIcon(icon)
        self.btn_fecha_diaria.setObjectName("btn_fecha_diaria")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(290, 90, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(340, 100, 221, 361))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.Btn_volver2 = QtWidgets.QPushButton(self.tab_2)
        self.Btn_volver2.setGeometry(QtCore.QRect(560, 470, 75, 23))
        self.Btn_volver2.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_volver2.setObjectName("Btn_volver2")
        self.Btn_ventas_mensuales = QtWidgets.QPushButton(self.tab_2)
        self.Btn_ventas_mensuales.setGeometry(QtCore.QRect(260, 100, 75, 23))
        self.Btn_ventas_mensuales.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_ventas_mensuales.setObjectName("Btn_ventas_mensuales")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(290, 10, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setGeometry(QtCore.QRect(40, 200, 861, 291))
        self.tableWidget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(8)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        self.search_nroFactura = QtWidgets.QLineEdit(self.tab_3)
        self.search_nroFactura.setGeometry(QtCore.QRect(472, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_nroFactura.setFont(font)
        self.search_nroFactura.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_nroFactura.setMaxLength(5)
        self.search_nroFactura.setObjectName("search_nroFactura")
        self.Boton_Buscar_nroFactura = QtWidgets.QPushButton(self.tab_3)
        self.Boton_Buscar_nroFactura.setGeometry(QtCore.QRect(570, 100, 31, 21))
        self.Boton_Buscar_nroFactura.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"")
        self.Boton_Buscar_nroFactura.setText("")
        self.Boton_Buscar_nroFactura.setIcon(icon)
        self.Boton_Buscar_nroFactura.setObjectName("Boton_Buscar_nroFactura")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(280, 100, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Btn_volver3 = QtWidgets.QPushButton(self.tab_3)
        self.Btn_volver3.setGeometry(QtCore.QRect(420, 510, 75, 23))
        self.Btn_volver3.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_volver3.setObjectName("Btn_volver3")
        self.Btn_listar = QtWidgets.QPushButton(self.tab_3)
        self.Btn_listar.setGeometry(QtCore.QRect(40, 170, 75, 23))
        self.Btn_listar.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_listar.setObjectName("Btn_listar")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(310, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.btn_buscar_fecha1 = QtWidgets.QPushButton(self.tab_3)
        self.btn_buscar_fecha1.setGeometry(QtCore.QRect(220, 100, 31, 21))
        self.btn_buscar_fecha1.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"")
        self.btn_buscar_fecha1.setText("")
        self.btn_buscar_fecha1.setIcon(icon)
        self.btn_buscar_fecha1.setObjectName("btn_buscar_fecha1")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(60, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.input_fecha = QtWidgets.QLineEdit(self.tab_3)
        self.input_fecha.setGeometry(QtCore.QRect(120, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.input_fecha.setFont(font)
        self.input_fecha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_fecha.setMaxLength(10)
        self.input_fecha.setObjectName("input_fecha")
        self.comboBox_pago = QtWidgets.QComboBox(self.tab_3)
        self.comboBox_pago.setGeometry(QtCore.QRect(760, 100, 141, 22))
        self.comboBox_pago.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.comboBox_pago.setObjectName("comboBox_pago")
        self.comboBox_pago.addItem("")
        self.comboBox_pago.addItem("")
        self.comboBox_pago.addItem("")
        self.comboBox_pago.addItem("")
        self.comboBox_pago.addItem("")
        self.comboBox_pago.addItem("")
        self.comboBox_pago.addItem("")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(630, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(190, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget_4.setEnabled(True)
        self.tableWidget_4.setGeometry(QtCore.QRect(160, 200, 331, 291))
        self.tableWidget_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_4.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        self.Btn_listar_2 = QtWidgets.QPushButton(self.tab_4)
        self.Btn_listar_2.setGeometry(QtCore.QRect(70, 200, 75, 23))
        self.Btn_listar_2.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_listar_2.setObjectName("Btn_listar_2")
        self.Btn_volver_4 = QtWidgets.QPushButton(self.tab_4)
        self.Btn_volver_4.setGeometry(QtCore.QRect(280, 510, 75, 23))
        self.Btn_volver_4.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_volver_4.setObjectName("Btn_volver_4")
        self.btn_imprimir = QtWidgets.QPushButton(self.tab_4)
        self.btn_imprimir.setGeometry(QtCore.QRect(60, 300, 91, 23))
        self.btn_imprimir.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.btn_imprimir.setObjectName("btn_imprimir")
        self.search_fecha = QtWidgets.QLineEdit(self.tab_4)
        self.search_fecha.setGeometry(QtCore.QRect(230, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_fecha.setFont(font)
        self.search_fecha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_fecha.setMaxLength(10)
        self.search_fecha.setObjectName("search_fecha")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(160, 100, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.btn_buscarFecha = QtWidgets.QPushButton(self.tab_4)
        self.btn_buscarFecha.setGeometry(QtCore.QRect(330, 100, 31, 21))
        self.btn_buscarFecha.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"")
        self.btn_buscarFecha.setText("")
        self.btn_buscarFecha.setIcon(icon)
        self.btn_buscarFecha.setObjectName("btn_buscarFecha")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(160, 150, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.comboBox_pago_2 = QtWidgets.QComboBox(self.tab_4)
        self.comboBox_pago_2.setGeometry(QtCore.QRect(290, 150, 141, 22))
        self.comboBox_pago_2.setStyleSheet("background-color: rgb(227, 227, 227);")
        self.comboBox_pago_2.setObjectName("comboBox_pago_2")
        self.comboBox_pago_2.addItem("")
        self.comboBox_pago_2.addItem("")
        self.comboBox_pago_2.addItem("")
        self.comboBox_pago_2.addItem("")
        self.comboBox_pago_2.addItem("")
        self.comboBox_pago_2.addItem("")
        self.comboBox_pago_2.addItem("")
        self.btn_anularVenta = QtWidgets.QPushButton(self.tab_4)
        self.btn_anularVenta.setGeometry(QtCore.QRect(650, 370, 91, 23))
        self.btn_anularVenta.setStyleSheet("background-color: rgb(218, 218, 218);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.btn_anularVenta.setObjectName("btn_anularVenta")
        self.input_motivo = QtWidgets.QTextEdit(self.tab_4)
        self.input_motivo.setGeometry(QtCore.QRect(550, 200, 300, 150))
        self.input_motivo.setMaximumSize(QtCore.QSize(300, 150))
        self.input_motivo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.input_motivo.setObjectName("input_motivo")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(550, 170, 251, 21))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.Btn_volver_5 = QtWidgets.QPushButton(self.tab_5)
        self.Btn_volver_5.setGeometry(QtCore.QRect(330, 470, 75, 23))
        self.Btn_volver_5.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_volver_5.setObjectName("Btn_volver_5")
        self.label_15 = QtWidgets.QLabel(self.tab_5)
        self.label_15.setGeometry(QtCore.QRect(370, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget_5.setEnabled(True)
        self.tableWidget_5.setGeometry(QtCore.QRect(200, 160, 331, 291))
        self.tableWidget_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_5.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(3)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        self.Btn_listar_3 = QtWidgets.QPushButton(self.tab_5)
        self.Btn_listar_3.setGeometry(QtCore.QRect(110, 160, 75, 23))
        self.Btn_listar_3.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_listar_3.setObjectName("Btn_listar_3")
        self.label = QtWidgets.QLabel(self.tab_5)
        self.label.setGeometry(QtCore.QRect(570, 120, 141, 31))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.btn_buscarComprobante = QtWidgets.QPushButton(self.tab_5)
        self.btn_buscarComprobante.setGeometry(QtCore.QRect(300, 100, 31, 21))
        self.btn_buscarComprobante.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"")
        self.btn_buscarComprobante.setText("")
        self.btn_buscarComprobante.setIcon(icon)
        self.btn_buscarComprobante.setObjectName("btn_buscarComprobante")
        self.search_comprobante = QtWidgets.QLineEdit(self.tab_5)
        self.search_comprobante.setGeometry(QtCore.QRect(210, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_comprobante.setFont(font)
        self.search_comprobante.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_comprobante.setMaxLength(5)
        self.search_comprobante.setPlaceholderText("")
        self.search_comprobante.setObjectName("search_comprobante")
        self.label_14 = QtWidgets.QLabel(self.tab_5)
        self.label_14.setGeometry(QtCore.QRect(50, 100, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.motivo_anulacion = QtWidgets.QTextEdit(self.tab_5)
        self.motivo_anulacion.setGeometry(QtCore.QRect(570, 160, 261, 150))
        self.motivo_anulacion.setMaximumSize(QtCore.QSize(300, 150))
        self.motivo_anulacion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.motivo_anulacion.setObjectName("motivo_anulacion")
        self.btn_verMotivo = QtWidgets.QPushButton(self.tab_5)
        self.btn_verMotivo.setGeometry(QtCore.QRect(760, 130, 75, 23))
        self.btn_verMotivo.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.btn_verMotivo.setObjectName("btn_verMotivo")
        self.tabWidget.addTab(self.tab_5, "")

        self.retranslateUi(informeDeVentas)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(informeDeVentas)

        self.a = self.Btn_Ver_Importes.clicked.connect(lambda:self.listarVentas.listarVentas())
        
        self.b = self.Btn_ventas_mensuales.clicked.connect(lambda:self.listarVentas.ventasMensuales())
        
        self.c = self.Btn_listar.clicked.connect(lambda:self.listarVentas.detalleVenta())
        
        self.d = self.Boton_Buscar_nroFactura.clicked.connect(lambda:self.listarVentas.buscarVentaXFactura(self.search_nroFactura.text()))
        
        self.e = self.Btn_Volver.clicked.connect(lambda:self.listarVentas.salir(informeDeVentas))
        
        self.f = self.Btn_volver2.clicked.connect(lambda:self.listarVentas.salir(informeDeVentas))
        
        self.g = self.Btn_volver3.clicked.connect(lambda:self.listarVentas.salir(informeDeVentas))
        
        self.h = self.Btn_listar_2.clicked.connect(lambda:self.listarVentas.buscarCondPago(self.comboBox_pago_2.currentText()))
        
        self.i = self.Btn_listar.clicked.connect(lambda:self.listarVentas.buscarCondPago_2(self.comboBox_pago.currentText()))
        
        self.j = self.btn_imprimir.clicked.connect(lambda:self.listarVentas.imprimirReporteVentas())
        
        self.k = self.btn_buscarFecha.clicked.connect(lambda:self.listarVentas.fechaVentaDiaria(self.search_fecha.text()))
        
        self.l = self.btn_fecha_diaria.clicked.connect(lambda:self.listarVentas.buscarfechaDiaria(self.input_fecha_diaria.text()))
       
        self.m = self.btn_buscar_fecha1.clicked.connect(lambda:self.listarVentas.fechaDetalle(self.input_fecha.text()))
        
        self.n = self.Btn_volver_4.clicked.connect(lambda:self.listarVentas.salir(informeDeVentas))

        self.o = self.btn_anularVenta.clicked.connect(lambda:self.listarVentas.anularVenta(self.input_motivo.toPlainText()))

        self.p = self.Btn_listar_3.clicked.connect(lambda:self.listarVentas.ventasAnuladas())
       
        self.q = self.btn_verMotivo.clicked.connect(lambda:self.listarVentas.showMotivo())

        self.r = self.btn_buscarComprobante.clicked.connect(lambda:self.listarVentas.buscarVentaAnulada(self.search_comprobante.text()))

        self.s = self.Btn_volver_5.clicked.connect(lambda:self.listarVentas.salir(informeDeVentas))

    def retranslateUi(self, informeDeVentas):
        _translate = QtCore.QCoreApplication.translate
        informeDeVentas.setWindowTitle(_translate("informeDeVentas", "Informe de ventas"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("informeDeVentas", "Fecha"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("informeDeVentas", "Importe"))
        self.Btn_Volver.setText(_translate("informeDeVentas", "Volver atras"))
        self.Btn_Ver_Importes.setText(_translate("informeDeVentas", "Listar Ventas"))
        self.label_4.setText(_translate("informeDeVentas", "Total Ventas Diarias"))
        self.input_fecha_diaria.setPlaceholderText(_translate("informeDeVentas", "AAAA-MM-DD"))
        self.label_10.setText(_translate("informeDeVentas", "Fecha:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("informeDeVentas", "Ventas Diarias"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("informeDeVentas", "Mes"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("informeDeVentas", "Importe"))
        self.Btn_volver2.setText(_translate("informeDeVentas", "Volver atras"))
        self.Btn_ventas_mensuales.setText(_translate("informeDeVentas", "Listar Ventas"))
        self.label_5.setText(_translate("informeDeVentas", "Total ventas mensuales"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("informeDeVentas", "Ventas Mensuales"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("informeDeVentas", "Fecha"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("informeDeVentas", "Nro Comprobante"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("informeDeVentas", "CodCliente"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("informeDeVentas", "CodProducto"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("informeDeVentas", "Cantidad"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("informeDeVentas", "Producto"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("informeDeVentas", "Precio Unitario"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("informeDeVentas", "Subtotal"))
        self.label_3.setText(_translate("informeDeVentas", " Nro de Comprobante"))
        self.Btn_volver3.setText(_translate("informeDeVentas", "Volver atras"))
        self.Btn_listar.setText(_translate("informeDeVentas", "Listar Ventas"))
        self.label_6.setText(_translate("informeDeVentas", "Detalle de ventas"))
        self.label_9.setText(_translate("informeDeVentas", "Fecha:"))
        self.input_fecha.setPlaceholderText(_translate("informeDeVentas", "AAAA-MM-DD"))
        self.comboBox_pago.setItemText(0, _translate("informeDeVentas", "Todos"))
        self.comboBox_pago.setItemText(1, _translate("informeDeVentas", "Efectivo"))
        self.comboBox_pago.setItemText(2, _translate("informeDeVentas", "Tarjeta de Débito"))
        self.comboBox_pago.setItemText(3, _translate("informeDeVentas", "Tarjeta de Credito"))
        self.comboBox_pago.setItemText(4, _translate("informeDeVentas", "Transferencia Bancaria"))
        self.comboBox_pago.setItemText(5, _translate("informeDeVentas", "Pago QR"))
        self.comboBox_pago.setItemText(6, _translate("informeDeVentas", "Cheque"))
        self.label_11.setText(_translate("informeDeVentas", "Condición Pago"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("informeDeVentas", "Detalle de Ventas"))
        self.label_7.setText(_translate("informeDeVentas", "Reporte de ventas"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("informeDeVentas", "Fecha"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("informeDeVentas", "Nro Comprobante"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("informeDeVentas", "Total"))
        self.Btn_listar_2.setText(_translate("informeDeVentas", "Listar Ventas"))
        self.Btn_volver_4.setText(_translate("informeDeVentas", "Volver atras"))
        self.btn_imprimir.setText(_translate("informeDeVentas", "Imprimir Reporte"))
        self.search_fecha.setPlaceholderText(_translate("informeDeVentas", "AAAA-MM-DD"))
        self.label_8.setText(_translate("informeDeVentas", "Fecha:"))
        self.label_12.setText(_translate("informeDeVentas", "Condición Pago"))
        self.comboBox_pago_2.setItemText(0, _translate("informeDeVentas", "Todos"))
        self.comboBox_pago_2.setItemText(1, _translate("informeDeVentas", "Efectivo"))
        self.comboBox_pago_2.setItemText(2, _translate("informeDeVentas", "Tarjeta de Débito"))
        self.comboBox_pago_2.setItemText(3, _translate("informeDeVentas", "Tarjeta de Credito"))
        self.comboBox_pago_2.setItemText(4, _translate("informeDeVentas", "Transferencia Bancaria"))
        self.comboBox_pago_2.setItemText(5, _translate("informeDeVentas", "Pago QR"))
        self.comboBox_pago_2.setItemText(6, _translate("informeDeVentas", "Cheque"))
        self.btn_anularVenta.setText(_translate("informeDeVentas", "Anular Venta"))
        self.input_motivo.setPlaceholderText(_translate("informeDeVentas", "Escriba aquí el motivo de anulación de venta"))
        self.label_2.setText(_translate("informeDeVentas", "Motivo de anulación de venta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("informeDeVentas", "Reporte de ventas "))
        self.Btn_volver_5.setText(_translate("informeDeVentas", "Volver atras"))
        self.label_15.setText(_translate("informeDeVentas", "Ventas Anuladas"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("informeDeVentas", "Fecha"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("informeDeVentas", "Nro Comprobante"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("informeDeVentas", "Total"))
        self.Btn_listar_3.setText(_translate("informeDeVentas", "Listar Venta"))
        self.label.setText(_translate("informeDeVentas", "Motivo"))
        self.label_14.setText(_translate("informeDeVentas", "Nro Comprobante"))
        self.btn_verMotivo.setText(_translate("informeDeVentas", "Ver motivo"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("informeDeVentas", "Ventas anuladas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    informeDeVentas = QtWidgets.QWidget()
    ui = Ui_informeDeVentas()
    ui.setupUi(informeDeVentas)
    informeDeVentas.show()
    sys.exit(app.exec_())
