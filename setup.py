import sys
import os

from cx_Freeze import setup, Executable

files= ['.vs', '.vscode', 'Controllers','Database','Imagenes','Models','Views','comprobanteVenta.pdf','listaStockBajo.pdf','ManualDeUsuarioSistemaTweety.pdf','reporteVentas.pdf']

exe=Executable(script= 'login_ui.py', base='Win32GUI')

setup(
    name='Sistema Tweety',
    version = '1.0',
    description = 'Aplicación de escritorio para punto de venta',
    author = 'Maximiliano Leloutre, Lucas Ortellado, Miguel Peña',
    options = {'build_exe':{'include_files':files}},
    executables=[exe]
)