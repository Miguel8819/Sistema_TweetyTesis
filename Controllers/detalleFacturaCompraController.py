import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Database.Connection import connection
from Models.facturaCompra import FacturaCompra

class detalleFacturaCompraController():
    def __init__(self, detalle_factCompra):
        self.factCompra = FacturaCompra(connection())
        self.detalle_factCompra = detalle_factCompra

    def displayFactura(self, nrofactura):
        factura = self.factCompra.getDetalleFactura(nrofactura)
        print(factura)
        if factura:
            self.detalle_factCompra.input_provFact.setText(str(factura[2]))
            self.detalle_factCompra.input_nroFac.setText(str(factura[3]))
            self.detalle_factCompra.input_nroCuil.setText(str(factura[4]))
            self.detalle_factCompra.input_fechaEmision.setText(str(factura[5]))
            self.detalle_factCompra.input_fechaEmision_2.setText(str(factura[6]))
            self.detalle_factCompra.input_tipoCompra.setText(str(factura[7]))
            self.detalle_factCompra.input_subtotal.setText(str(factura[8]))
            self.detalle_factCompra.input_descuento_2.setText(str(factura[9]))
            self.detalle_factCompra.input_iva.setText(str(factura[10]))
            self.detalle_factCompra.input_importe.setText(str(factura[11]))
