import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.menuprincipalController import menuprincipalController
from venta_ui import Ui_venta
from controlstock_ui import Ui_controlstock
from proveedores_ui import Ui_Proveedores
from createproduct_ui import Ui_CreateProduct
from cliente_ui import Ui_clientes
from listadeclientes_ui import Ui_lista_clientes
from gestionClaves_ui import Ui_LogIn
from gestionBackup_ui import Ui_Backup
from listadeproveedores_ui import Ui_lista_proveedores
from informedeventas_ui import Ui_informeDeVentas
from facturaCompra_ui import Ui_FacturaDeCompra


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
        self.btn_mantenimiento.setGeometry(QtCore.QRect(11, 342, 209, 50))
        self.btn_mantenimiento.setMinimumSize(QtCore.QSize(209, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_mantenimiento.setFont(font)
        self.btn_mantenimiento.setLayoutDirection(QtCore.Qt.RightToLeft)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mantenimiento.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("comprar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon2.addPixmap(QtGui.QPixmap("punto-de-venta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon3.addPixmap(QtGui.QPixmap("en-stock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_gestionStock.setIcon(icon3)
        self.btn_gestionStock.setIconSize(QtCore.QSize(35, 35))
        self.btn_gestionStock.setObjectName("btn_gestionStock")
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
        self.label_8.setPixmap(QtGui.QPixmap("comprar.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.btn_genOrdenCompra = QtWidgets.QPushButton(self.page_gestionCompra)
        self.btn_genOrdenCompra.setGeometry(QtCore.QRect(130, 250, 290, 50))
        self.btn_genOrdenCompra.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_genOrdenCompra.setFont(font)
        self.btn_genOrdenCompra.setObjectName("btn_genOrdenCompra")
        self.btn_listaproveedores = QtWidgets.QPushButton(self.page_gestionCompra)
        self.btn_listaproveedores.setGeometry(QtCore.QRect(130, 180, 290, 50))
        self.btn_listaproveedores.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_listaproveedores.setFont(font)
        self.btn_listaproveedores.setObjectName("btn_listaproveedores")
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
        self.label_9.setPixmap(QtGui.QPixmap("punto-de-venta.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
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
        self.btn_dbClientes.setGeometry(QtCore.QRect(131, 182, 290, 50))
        self.btn_dbClientes.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_dbClientes.setFont(font)
        self.btn_dbClientes.setObjectName("btn_dbClientes")
        self.btn_listaClientes = QtWidgets.QPushButton(self.page_gestionVenta)
        self.btn_listaClientes.setGeometry(QtCore.QRect(130, 262, 290, 50))
        self.btn_listaClientes.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_listaClientes.setFont(font)
        self.btn_listaClientes.setObjectName("btn_listaClientes")
        self.btn_infDeVentas = QtWidgets.QPushButton(self.page_gestionVenta)
        self.btn_infDeVentas.setGeometry(QtCore.QRect(130, 342, 290, 50))
        self.btn_infDeVentas.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_infDeVentas.setFont(font)
        self.btn_infDeVentas.setObjectName("btn_infDeVentas")
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
        self.btn_controlStock.setGeometry(QtCore.QRect(130, 180, 290, 50))
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
        self.label_5.setPixmap(QtGui.QPixmap("en-stock.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.btn_abmProd = QtWidgets.QPushButton(self.page_gestionStock)
        self.btn_abmProd.setGeometry(QtCore.QRect(130, 100, 290, 50))
        self.btn_abmProd.setMinimumSize(QtCore.QSize(290, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abmProd.setFont(font)
        self.btn_abmProd.setObjectName("btn_abmProd")
        self.stackedWidget.addWidget(self.page_gestionStock)
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
        self.label_11.setPixmap(QtGui.QPixmap("mantenimiento.png"))
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
        self.btn_mantenimiento.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_mantenimiento))
        self.btn_proveedores.clicked.connect(lambda:self.menuprincipalController.openProveedores(Ui_Proveedores, menuprincipal))
        self.btn_controlStock.clicked.connect(lambda:self.menuprincipalController.openControlStock(Ui_controlstock, menuprincipal))
        self.btn_facturacion.clicked.connect(lambda:self.menuprincipalController.openFacturacion(Ui_venta, menuprincipal))
        self.btn_abmProd.clicked.connect(lambda:self.menuprincipalController.openCreateProduct(Ui_CreateProduct, menuprincipal))
        self.btn_dbClientes.clicked.connect(lambda:self.menuprincipalController.openClientes(Ui_clientes, menuprincipal))
        self.btn_movFondos_2.clicked.connect(lambda:self.menuprincipalController.openGestionClaves(Ui_LogIn, menuprincipal))
        self.btn_abrirCerrarCaja_2.clicked.connect(lambda: self.menuprincipalController.openGestionBackup(Ui_Backup, menuprincipal))
        self.btn_listaClientes.clicked.connect(lambda:self.menuprincipalController.openListaClientes(Ui_lista_clientes, menuprincipal))
        self.btn_listaproveedores.clicked.connect(lambda:self.menuprincipalController.openListaProveedores(Ui_lista_proveedores, menuprincipal))
        self.btn_infDeVentas.clicked.connect(lambda:self.menuprincipalController.openInformeDeVentas(Ui_informeDeVentas, menuprincipal))
        self.btn_genOrdenCompra.clicked.connect(lambda:self.menuprincipalController.openFacturaCompra(Ui_FacturaDeCompra, menuprincipal))

#--------------------End Events---------------------------------


    def retranslateUi(self, menuprincipal):
        _translate = QtCore.QCoreApplication.translate
        menuprincipal.setWindowTitle(_translate("menuprincipal", "Menú Principal"))
        self.label_6.setText(_translate("menuprincipal", "Sistema Tweety"))
        self.btn_mantenimiento.setText(_translate("menuprincipal", "Mantenimiento"))
        self.btn_gestionCompra.setText(_translate("menuprincipal", "Gestión de Compra"))
        self.btn_gestionVenta.setText(_translate("menuprincipal", "Gestión de Venta"))
        self.btn_gestionStock.setText(_translate("menuprincipal", "Gestión de Stock"))
        self.label.setText(_translate("menuprincipal", "Gestión de Compra"))
        self.btn_proveedores.setText(_translate("menuprincipal", "ABM Proveedores"))
        self.btn_genOrdenCompra.setText(_translate("menuprincipal", "Ingresar Factura de Compra"))
        self.btn_listaproveedores.setText(_translate("menuprincipal", "Lista de Proveedores"))
        self.label_2.setText(_translate("menuprincipal", "Gestión de Venta"))
        self.btn_facturacion.setText(_translate("menuprincipal", "Facturación"))
        self.btn_dbClientes.setText(_translate("menuprincipal", "ABM Clientes"))
        self.btn_listaClientes.setText(_translate("menuprincipal", "Lista de Clientes"))
        self.btn_infDeVentas.setText(_translate("menuprincipal", "Informe de Ventas"))
        self.label_3.setText(_translate("menuprincipal", "Gestión de Stock"))
        self.btn_controlStock.setText(_translate("menuprincipal", "Lista de productos"))
        self.btn_abmProd.setText(_translate("menuprincipal", "ABM Productos"))
        self.label_12.setText(_translate("menuprincipal", "Mantenimiento"))
        self.btn_movFondos_2.setText(_translate("menuprincipal", "Gestion de Clave"))
        self.btn_infDeCaja_2.setText(_translate("menuprincipal", "Manual de Usuario"))
        self.btn_abrirCerrarCaja_2.setText(_translate("menuprincipal", "Gestion de Backup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menuprincipal = QtWidgets.QWidget()
    ui = Ui_menuprincipal()
    ui.setupUi(menuprincipal)
    menuprincipal.show()
    sys.exit(app.exec_())
