import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.venta import Venta
from Models.cabeceraFactura import CabeceraFactura
from PyQt5.QtWidgets import QMessageBox
from fpdf import FPDF
from functools import reduce
from Controllers import globales


class listarVentas():
    def __init__(self, listar_VentasDiarias):
        self.venta = Venta(connection())
        self.cabeceraFactura = CabeceraFactura(connection())
        self.listar_ventasDiarias = listar_VentasDiarias
        self.usuario = globales.logueado      

    def listarVentas(self):
        table = self.listar_ventasDiarias.tableWidget
        ventasDiarias = self.venta.ventasDiarias()
        if ventasDiarias:   
            table.setRowCount(0)
            for row_number, row_data in enumerate(ventasDiarias):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                        
        else:
            self.listar_ventasDiarias.tableWidget.setRowCount(0)
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Aún no hay ventas.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()

    def detalleVenta(self):
        table = self.listar_ventasDiarias.tableWidget_3
        ventasDiarias = self.venta.detalleVentas()
        if ventasDiarias:   
            table.setRowCount(0)
            for row_number, row_data in enumerate(ventasDiarias):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            self.listar_ventasDiarias.tableWidget_3.setRowCount(0)
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Aún no hay ventas.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()
            
    def ventasMensuales(self):
        table = self.listar_ventasDiarias.tableWidget_2
        ventasMensuales = self.venta.ventasMensuales()
        if ventasMensuales:   
            table.setRowCount(0)
            for row_number, row_data in enumerate(ventasMensuales):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            self.listar_ventasDiarias.tableWidget_2.setRowCount(0)
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Aún no hay ventas.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()

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
                msg.setText("El número de comprobante no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Escriba un número de comprobante")
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
        if lista_datos:    
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
            pdf.cell(w = 50, h = 7, txt = 'N° de Comprobante', border = 1,
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
        else:
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("La lista esta vacia.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()
    
    def listarReporte(self):
        table = self.listar_ventasDiarias.tableWidget_4
        ventasDiarias = self.venta.imprimirVentas()   
        if ventasDiarias:
            table.setRowCount(0)
            for row_number, row_data in enumerate(ventasDiarias):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Aún no hay ventas.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()

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

    def buscarCondPago(self,condPago):
        table = self.listar_ventasDiarias.tableWidget_4 
        if condPago !='Todos':    
            ventaDiaria= self.venta.condPago(condPago)
            if ventaDiaria:
                table.setRowCount(0)
                for row_number, row_data in enumerate(ventaDiaria):
                        table.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else: 
                self.listar_ventasDiarias.tableWidget_4.setRowCount(0) 
                msg = QMessageBox()
                msg.setWindowTitle('¡Error!')
                msg.setText("Aún no hay ventas.")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()
        
            
        elif condPago:
            table = self.listar_ventasDiarias.tableWidget_4 
            ventaDiaria= self.venta.condPagoTodos()
            if ventaDiaria:
                table.setRowCount(0)
                for row_number, row_data in enumerate(ventaDiaria):
                        table.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else: 
                self.listar_ventasDiarias.tableWidget_4.setRowCount(0) 
                msg = QMessageBox()
                msg.setWindowTitle('¡Error!')
                msg.setText("Aún no hay ventas.")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()
        
    def buscarCondPago_2(self,condPago):
        table = self.listar_ventasDiarias.tableWidget_3 
        if condPago !='Todos':    
            ventaDiaria= self.venta.condPago_2(condPago)
            if ventaDiaria:
                table.setRowCount(0)
                for row_number, row_data in enumerate(ventaDiaria):
                        table.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else: 
                self.listar_ventasDiarias.tableWidget_3.setRowCount(0) 
		 	
        elif condPago:
            table = self.listar_ventasDiarias.tableWidget_3 
            ventaDiaria= self.venta.condPagoTodos_2()
            if ventaDiaria:
                table.setRowCount(0)
                for row_number, row_data in enumerate(ventaDiaria):
                        table.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def refrescarAnulacion(self,condPago):
        table = self.listar_ventasDiarias.tableWidget_4 
        if condPago !='Todos':    
            ventaDiaria= self.venta.condPago(condPago)
            if ventaDiaria:
                table.setRowCount(0)
                for row_number, row_data in enumerate(ventaDiaria):
                        table.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else: 
                self.listar_ventasDiarias.tableWidget_4.setRowCount(0) 
            
        elif condPago:
            table = self.listar_ventasDiarias.tableWidget_4 
            ventaDiaria= self.venta.condPagoTodos()
            if ventaDiaria:
                table.setRowCount(0)
                for row_number, row_data in enumerate(ventaDiaria):
                        table.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else: 
                self.listar_ventasDiarias.tableWidget_4.setRowCount(0) 
                       
    def anularVenta (self,motivo):
        table = self.listar_ventasDiarias.tableWidget_4
        if table.currentItem() != None:
            nroFactura = table.currentItem().text()        
            venta = self.venta.ventaPorFactura(nroFactura)
                    
            if venta:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Esta seguro de anular la venta? ")
                msgBox.setWindowTitle("Confirmacion")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    if motivo:
                        self.cabeceraFactura.insertMotivo(motivo,nroFactura,self.usuario[0]) 
                        self.venta.anular_venta(nroFactura) 
                        self.refrescarAnulacion(condPago='Todos')
                        self.listar_ventasDiarias.input_motivo.clear() 

                        msg = QMessageBox()
                        msg.setWindowTitle('¡Exito!')
                        msg.setText("¡Venta anulada!.")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        x = msg.exec_()
                        
                    else:
                        msg = QMessageBox()
                        msg.setWindowTitle('¡Error!')
                        msg.setText("Por favor escriba el motivo de la anulación de venta y luego presione el botón Anular Venta.")
                        msg.setIcon(QMessageBox.Information)
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setDefaultButton(QMessageBox.Ok)
                        x = msg.exec_()

            else:
                msg = QMessageBox()
                msg.setWindowTitle('¡Error!')
                msg.setText("Seleccione el número de comprobante y luego presione el boton Anular Venta.")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Seleccione el número de comprobante para anular la venta.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()
    
    def ventasAnuladas(self):
        
        table = self.listar_ventasDiarias.tableWidget_5
        ventasDiarias = self.venta.listarVentasAnuladas()
        if ventasDiarias:
            table.setRowCount(0)
            for row_number, row_data in enumerate(ventasDiarias):
                    table.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("No hay ventas anuladas.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()

    def buscarVentaAnulada(self,nroFactura):
        table = self.listar_ventasDiarias.tableWidget_5
        if nroFactura:
            ventaDiaria= self.venta.buscarAnulada(nroFactura)
            if ventaDiaria:
                table.setRowCount(0)
                for row_number, row_data in enumerate(ventaDiaria):
                        table.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("El numero de comprobante no existe")
                msg.setIcon(QMessageBox.Information)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)
                msg.setInformativeText("Vuelva a intentarlo")
                x = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Escriba un numero de comprobante")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()

    def detalleAnulada(self):
        table = self.listar_ventasDiarias.tableWidget_5
        if table.currentItem() != None:
            nroFactura = table.currentItem().text()        
            self.venta.ventaPorFactura(nroFactura)
            if nroFactura:
                ventasDiarias = self.venta.showDetalleAnulada(nroFactura)
                if ventasDiarias: 
                    table = self.listar_ventasDiarias.tableWidget_6  
                    table.setRowCount(0)
                    for row_number, row_data in enumerate(ventasDiarias):
                            table.insertRow(row_number)
                            for column_number, data in enumerate(row_data):
                                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        else:
            self.listar_ventasDiarias.tableWidget_6.setRowCount(0)
            msg = QMessageBox()
            msg.setWindowTitle('¡Error!')
            msg.setText("Aún no hay ventas.")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            x = msg.exec_()

    def showMotivo(self):
        table = self.listar_ventasDiarias.tableWidget_5
        if table.currentItem() != None:
            nroFactura = table.currentItem().text()        
            self.venta.ventaPorFactura(nroFactura)
            if nroFactura:
                result = self.cabeceraFactura.getNroFactura(nroFactura)
                if result:
                    self.listar_ventasDiarias.motivo_anulacion.setText(str(result[4]))
                    self.detalleAnulada()
                else:    
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Seleccione un nro de Comprobante")
                    msg.setIcon(QMessageBox.Information)
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setDefaultButton(QMessageBox.Ok)
                    msg.setInformativeText("Vuelva a intentarlo")
                    x = msg.exec_()
        else:    
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Seleccione un nro de Comprobante")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_()

    def limpiar1 (self):
        self.listar_ventasDiarias.tableWidget.setRowCount(0)
        self.listar_ventasDiarias.input_fecha_diaria.clear()
        
    def limpiar2 (self):
        self.listar_ventasDiarias.tableWidget_2.setRowCount(0)
        
    def limpiar3 (self):
        self.listar_ventasDiarias.tableWidget_3.setRowCount(0)
        self.listar_ventasDiarias.input_fecha.clear()
        self.listar_ventasDiarias.search_nroFactura.clear()
    
    def limpiar4 (self):
        self.listar_ventasDiarias.tableWidget_4.setRowCount(0)
        self.listar_ventasDiarias.search_fecha.clear()
        self.listar_ventasDiarias.input_motivo.clear()
        
    def limpiar5 (self):
        self.listar_ventasDiarias.tableWidget_5.setRowCount(0)
        self.listar_ventasDiarias.tableWidget_6.setRowCount(0)
        self.listar_ventasDiarias.search_comprobante.clear()
        self.listar_ventasDiarias.motivo_anulacion.clear()    

    def salir(self, listar_ventasDiarias):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("¿Desea salir?")
        msgBox.setWindowTitle("Informe de ventas")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            listar_ventasDiarias.close()
