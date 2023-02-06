import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Database.Connection import connection
from Models.facturaCompra import FacturaCompra
from Controllers import globales

class detalleFacturaCompraController():
    def __init__(self, detalle_factCompra):
        self.factCompra = FacturaCompra(connection())
        self.detalle_factCompra = detalle_factCompra
        self.usuario = globales.logueado 
   

    def buscarFactNombreProv(self, nameProv):
        table = self.detalle_factCompra.tabla_compra
        facturas = self.factCompra.getFactByProv(nameProv)
        table.setRowCount(0)
        for row_number, row_data in enumerate(facturas):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def buscarFactNumFact(self, numFact):
        table = self.detalle_factCompra.tabla_compra
        facturas = self.factCompra.getFactByNum(numFact)
        table.setRowCount(0)
        for row_number, row_data in enumerate(facturas):
            table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def openDetalleFactura(self):
        try:
            table = self.detalle_factCompra.tabla_compra
            nrofact = table.currentItem().text()
        except: 
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No ha seleccionado un numero de factura de la tabla")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_() 
        else:    
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea ver detalle de la factura seleccionada?")
            msgBox.setWindowTitle("Abrir Detalle Factura")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                factura = self.factCompra.getDetalleFactura(nrofact)
                detalle_factura = self.factCompra.getDetalleTablaFactura(nrofact)
                if factura and detalle_factura:
                    self.detalle_factCompra.input_facCompra.setText(str(factura[0][1]))
                    self.detalle_factCompra.input_provFact.setText(str(factura[0][2]))
                    self.detalle_factCompra.input_nroFac.setText(str(factura[0][3]))
                    self.detalle_factCompra.input_nroCuil.setText(str(factura[0][4]))
                    self.detalle_factCompra.input_fechaEmision.setText(str(factura[0][5]))
                    self.detalle_factCompra.input_fechaEmision_2.setText(str(factura[0][6]))
                    self.detalle_factCompra.input_tipoCompra.setText(str(factura[0][7]))
                    self.detalle_factCompra.input_subtotal.setText(str(factura[0][8]))
                    self.detalle_factCompra.input_descuento_2.setText(str(factura[0][9]))
                    self.detalle_factCompra.input_iva.setText(str(factura[0][10]))
                    self.detalle_factCompra.input_importe.setText(str(factura[0][11]))

                    table_detalle = self.detalle_factCompra.table_detalleCompra
                    table_detalle.setRowCount(0)
                    for row_number, row_data in enumerate(detalle_factura):
                        table_detalle.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table_detalle.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

    def anularFactura (self,motivo):
        table = self.detalle_factCompra.tabla_compra
        if table.currentItem() != None:
            nroFactura = table.currentItem().text()        
            compra = self.factCompra.getDetalleFactura(nroFactura)
                    
            if compra:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("¿Esta seguro de anular la compra? ")
                msgBox.setWindowTitle("Confirmacion")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Ok:
                    if motivo:
                        self.factCompra.insertMotivoCompra(motivo,nroFactura,self.usuario[0]) 
                        self.factCompra.anular_compra(nroFactura) 
                       
                        self.detalle_factCompra.textMotivo.clear() 
                        self.detalle_factCompra.input_facCompra.clear() 
                        self.detalle_factCompra.input_nroFac.clear() 
                        self.detalle_factCompra.input_fechaEmision.clear()
                        self.detalle_factCompra.input_fechaEmision_2.clear()
                        self.detalle_factCompra.input_provFact.clear()
                        self.detalle_factCompra.input_nroCuil.clear()
                        self.detalle_factCompra.input_tipoCompra.clear()
                        self.detalle_factCompra.table_detalleCompra.setRowCount(0)
                        nameProv = self.detalle_factCompra.input_provFact_2.text() 
                        self.buscarFactNombreProv(nameProv)
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

    def comprasAnuladas(self):
        
        table = self.detalle_factCompra.tabla_compra_2
        listaAnuladas = self.factCompra.getAnuladas()
        if listaAnuladas:
            table.setRowCount(0)
            for row_number, row_data in enumerate(listaAnuladas):
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

    def detalleCompraAnulada(self):
        try:
            table = self.detalle_factCompra.tabla_compra_2
            nrofact = table.currentItem().text()
        except: 
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("No ha seleccionado un numero de factura de la tabla")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.setInformativeText("Vuelva a intentarlo")
            x = msg.exec_() 
        else:    
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("¿Desea ver detalle de la factura seleccionada?")
            msgBox.setWindowTitle("Abrir Detalle Factura")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                
                detalle_factura = self.factCompra.getDetalleTablaFactura(nrofact)
                if  detalle_factura:
                    table_detalle = self.detalle_factCompra.table_detalleCompra_2
                    table_detalle.setRowCount(0)
                    for row_number, row_data in enumerate(detalle_factura):
                        table_detalle.insertRow(row_number)
                        for column_number, data in enumerate(row_data):
                            table_detalle.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def showMotivoAnulacion(self):
        table = self.detalle_factCompra.tabla_compra_2
        if table.currentItem() != None:
            nroFactura = table.currentItem().text()        
            self.factCompra.getDetalleTablaFactura(nroFactura)
            if nroFactura:
                result = self.factCompra.getFactura(nroFactura)
                
                if result:
                    self.detalle_factCompra.textMotivo_2.setText(str(result[13]))
                    
                    self.detalleCompraAnulada()
                    self.detalle_factCompra.input_subtotal_2.setText(str(result[8]))
                    self.detalle_factCompra.input_descuento_3.setText(str(result[9]))
                    self.detalle_factCompra.input_iva_2.setText(str(result[10]))
                    self.detalle_factCompra.input_importe_2.setText(str(result[11]))
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


    def Salir(self,lista_factCompra):
        lista_factCompra.close()

