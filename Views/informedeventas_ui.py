# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'informedeventas.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_informeDeVentas(object):
    def setupUi(self, informeDeVentas):
        informeDeVentas.setObjectName("informeDeVentas")
        informeDeVentas.resize(888, 565)
        informeDeVentas.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.tabWidget = QtWidgets.QTabWidget(informeDeVentas)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 881, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(270, 110, 211, 391))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 30, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.search_fecha = QtWidgets.QLineEdit(self.tab)
        self.search_fecha.setGeometry(QtCore.QRect(200, 30, 113, 21))
        self.search_fecha.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_fecha.setObjectName("search_fecha")
        self.Boton_Buscar = QtWidgets.QPushButton(self.tab)
        self.Boton_Buscar.setGeometry(QtCore.QRect(320, 30, 31, 21))
        self.Boton_Buscar.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"")
        self.Boton_Buscar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/vector-find-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Boton_Buscar.setIcon(icon)
        self.Boton_Buscar.setObjectName("Boton_Buscar")
        self.Btn_Volver = QtWidgets.QPushButton(self.tab)
        self.Btn_Volver.setGeometry(QtCore.QRect(560, 450, 75, 23))
        self.Btn_Volver.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_Volver.setObjectName("Btn_Volver")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(250, 70, 171, 361))
        self.tableWidget_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setRowCount(11)
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
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.Btn_volver2 = QtWidgets.QPushButton(self.tab_2)
        self.Btn_volver2.setGeometry(QtCore.QRect(500, 410, 75, 23))
        self.Btn_volver2.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_volver2.setObjectName("Btn_volver2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setGeometry(QtCore.QRect(80, 130, 711, 291))
        self.tableWidget_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(7)
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
        self.search_fecha_2 = QtWidgets.QLineEdit(self.tab_3)
        self.search_fecha_2.setGeometry(QtCore.QRect(180, 40, 113, 21))
        self.search_fecha_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_fecha_2.setObjectName("search_fecha_2")
        self.Boton_Buscar_2 = QtWidgets.QPushButton(self.tab_3)
        self.Boton_Buscar_2.setGeometry(QtCore.QRect(300, 40, 31, 21))
        self.Boton_Buscar_2.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"")
        self.Boton_Buscar_2.setText("")
        self.Boton_Buscar_2.setIcon(icon)
        self.Boton_Buscar_2.setObjectName("Boton_Buscar_2")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(110, 40, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.search_nroFactura = QtWidgets.QLineEdit(self.tab_3)
        self.search_nroFactura.setGeometry(QtCore.QRect(520, 40, 113, 21))
        self.search_nroFactura.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_nroFactura.setObjectName("search_nroFactura")
        self.Boton_Buscar_3 = QtWidgets.QPushButton(self.tab_3)
        self.Boton_Buscar_3.setGeometry(QtCore.QRect(640, 40, 31, 21))
        self.Boton_Buscar_3.setStyleSheet("background-color: rgb(195, 195, 195);\n"
"")
        self.Boton_Buscar_3.setText("")
        self.Boton_Buscar_3.setIcon(icon)
        self.Boton_Buscar_3.setObjectName("Boton_Buscar_3")
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(380, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Btn_volver3 = QtWidgets.QPushButton(self.tab_3)
        self.Btn_volver3.setGeometry(QtCore.QRect(420, 440, 75, 23))
        self.Btn_volver3.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.Btn_volver3.setObjectName("Btn_volver3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(informeDeVentas)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(informeDeVentas)

    def retranslateUi(self, informeDeVentas):
        _translate = QtCore.QCoreApplication.translate
        informeDeVentas.setWindowTitle(_translate("informeDeVentas", "Informe de ventas"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("informeDeVentas", "Fecha"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("informeDeVentas", "Importe"))
        self.label.setText(_translate("informeDeVentas", "Buscar por Fecha"))
        self.Btn_Volver.setText(_translate("informeDeVentas", "Volver atras"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("informeDeVentas", "Ventas Diarias"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("informeDeVentas", "Enero"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("informeDeVentas", "Febrero"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("informeDeVentas", "Marzo"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("informeDeVentas", "Abril"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("informeDeVentas", "Mayo"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("informeDeVentas", "Junio"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("informeDeVentas", "Julio"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("informeDeVentas", "Agosto"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("informeDeVentas", "Septiembre"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("informeDeVentas", "Octubre"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("informeDeVentas", "Diciembre"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("informeDeVentas", "Importe"))
        self.Btn_volver2.setText(_translate("informeDeVentas", "Volver atras"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("informeDeVentas", "Ventas Mensuales"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("informeDeVentas", "Fecha"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("informeDeVentas", "Nro Factura"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("informeDeVentas", "Codigo"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("informeDeVentas", "Cantidad"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("informeDeVentas", "Producto"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("informeDeVentas", "Precio Unitario"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("informeDeVentas", "Subtotal"))
        self.label_2.setText(_translate("informeDeVentas", " Fecha"))
        self.label_3.setText(_translate("informeDeVentas", " Nro de Factura"))
        self.Btn_volver3.setText(_translate("informeDeVentas", "Volver atras"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("informeDeVentas", "Detalle de Ventas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    informeDeVentas = QtWidgets.QWidget()
    ui = Ui_informeDeVentas()
    ui.setupUi(informeDeVentas)
    informeDeVentas.show()
    sys.exit(app.exec_())
