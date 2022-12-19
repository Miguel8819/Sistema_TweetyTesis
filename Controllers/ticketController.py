from ipaddress import summarize_address_range
from locale import currency
import numbers
from re import sub
from sqlite3 import Row
import sys
import os
from this import s
from tkinter import CURRENT
from tokenize import Number
from datetime import datetime
from unittest import result


from Models.cabeceraFactura import CabeceraFactura



myDir = os.getcwd()
sys.path.append(myDir)
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtWidgets,QtCore,QtGui
from Database.Connection import connection
from Models.Product import Product
from Models.venta import Venta
from Models.cliente import *

class ticketController():
    
   
    
    

    def __init__(self, ticketFactura):
        self.product = Product(connection())
        self.ticketFactura = ticketFactura
        self.Venta = Venta(connection())
        self.Facturacion = CabeceraFactura(connection())
        self.cliente= Cliente(connection())

    def openT(self,Ui_TicketFactura):
        
        self.ticketFactura.Form = QtWidgets.QWidget()
        self.ticketFactura.ui = Ui_TicketFactura()
        self.ticketFactura.ui.setupUi(self.venta.Form)
        self.ticketFactura.Form.show() 

    def ticket(self,nroFactura):
       result=self.Facturacion.getNroFactura(nroFactura)
       if result:             
            self.TicketFactura.input_nroTicket.setText(str(result[0]))
            self.TicketFactura.input_fecha.setText(str(result[1]))