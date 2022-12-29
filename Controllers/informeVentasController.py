import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.venta import Venta
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QStringListModel, Qt
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QMessageBox
from fpdf import FPDF
from functools import reduce


class listarVentas():
    def __init__(self, listar_VentasDiarias):
        self.venta = Venta(connection())
        self.listar_ventasDiarias = listar_VentasDiarias
       

    def listarVentas(self):
        table = self.listar_ventasDiarias.tableWidget
        ventasDiarias = self.venta.ventasDiarias()
           
        table.setRowCount(0)
        for row_number, row_data in enumerate(ventasDiarias):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def detalleVenta(self):
        table = self.listar_ventasDiarias.tableWidget_3
        ventasDiarias = self.venta.detalleVentas()
           
        table.setRowCount(0)
        for row_number, row_data in enumerate(ventasDiarias):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def ventasMensuales(self):
        table = self.listar_ventasDiarias.tableWidget_2
        ventasMensuales = self.venta.ventasMensuales()
           
        table.setRowCount(0)
        for row_number, row_data in enumerate(ventasMensuales):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def fechaVentaDiaria(self,fecha):
        table = self.listar_ventasDiarias.tableWidget_4 
        if fecha:    
            ventaDiaria= self.venta.ventaPorFecha(fecha)
            if ventaDiaria:        
                    table.setRowCount(0)
                    for row_number, row_data in enumerate(ventaDiaria):
                            table.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Escriba una fecha válida")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()  
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Escriba una fecha. Por ejemplo: 2022-12-24")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()

    def buscarVentaXFactura(self,nroFactura):
        table = self.listar_ventasDiarias.tableWidget_3
        if nroFactura:
            ventaDiaria= self.venta.ventaPorFactura(nroFactura)
            if ventaDiaria:
                table.setRowCount(0)
                for row_number, row_data in enumerate(ventaDiaria):
                        table.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El numero de Factura no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Escriba un numero de factura")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()
    
    def imprimirReporteVentas(self):
        table = self.listar_ventasDiarias.tableWidget_4    
        lista_datos = []
        for  i in range(table.rowCount()):    
            lista_datos.append(( table.item(i,0).text(),table.item(i,1).text(), table.item(i,2).text()))
        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4') 
        pdf.set_margins(20, 10 , 10)
        pdf.set_auto_page_break(25)
        pdf.add_page()
        # TEXTO
        pdf.set_font('Arial', '', 15)
        pdf.cell(w = 0, h = 7, txt = 'Reporte de Ventas Diarias', border = 1, ln=1,
                                align = 'C', fill = 0)
        pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                align = 'C', fill = 0)
        pdf.set_font('Times', '', 28)
        pdf.cell(w = 50, h = 10, txt = 'Libreria Tweety', border = 0, ln=1,
                align = 'L', fill = 0)
        pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                align = 'C', fill = 0)
        pdf.cell(w = 0, h = 5, txt = '', border = 0, ln=1,
                align = 'C', fill = 0)
        pdf.set_font('Arial', '', 16)
        pdf.cell(w = 50, h = 7, txt = 'Fecha', border = 1,
                                align = 'C', fill = 0)
        pdf.cell(w = 50, h = 7, txt = 'Número de Factura', border = 1,
                align = 'C', fill = 0)
        pdf.multi_cell(w = 0, h = 7, txt = 'Importe', border = 1,
                align = 'C', fill = 0)
        # valores
        total = 0
        for valor in lista_datos:
                pdf.set_font('Arial', '', 10)    
                pdf.cell(w = 50, h = 5, txt = str(valor[0]), border = 0,
                        align = 'C', fill = 0)
                pdf.cell(w = 50, h = 5, txt = str(valor[1]), border = 0,
                        align = 'C', fill = 0)
                pdf.multi_cell(w = 0, h = 5, txt ='$' + str(valor[2]), border = 0,
                        align = 'C', fill = 0)                        
                total = total + float(valor[2])
         # reduce(lambda x, y: x + y, valores)       
        new = reduce(lambda x, y: x + y,list(map(lambda x : float(x[2]), lista_datos)))      
        print(total)  
        pdf.set_font('Arial', '', 15)
        pdf.cell(w = 0, h = 20, txt = 'Importe Total: $'+str(total), border = 0, ln=1,
                align = 'R', fill = 0)
        pdf.output('reporteVentas.pdf')
        os.startfile('reporteVentas.pdf') 
    
    def listarReporte(self):
        table = self.listar_ventasDiarias.tableWidget_4
        ventasDiarias = self.venta.imprimirVentas()       
        table.setRowCount(0)
        for row_number, row_data in enumerate(ventasDiarias):
                table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def fechaDetalle(self,fecha):
        table = self.listar_ventasDiarias.tableWidget_3 
        if fecha:    
            ventaDiaria= self.venta.detalleFecha(fecha)
            if ventaDiaria:
                table.setRowCount(0)
                for row_number, row_data in enumerate(ventaDiaria):
                        table.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Escriba una fecha válida")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()  
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Escriba una fecha. Por ejemplo: 2022-12-24")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()

    def buscarfechaDiaria(self,fecha):
        table = self.listar_ventasDiarias.tableWidget 
        if fecha:    
            ventaDiaria= self.venta.importeYfecha(fecha)
            if ventaDiaria:        
                    table.setRowCount(0)
                    for row_number, row_data in enumerate(ventaDiaria):
                            table.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                    table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Escriba una fecha válida")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()  
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Escriba una fecha. Por ejemplo: 2022-12-24")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()

    def salir(self, listar_ventasDiarias):
        listar_ventasDiarias.close()
