

class Venta():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS venta
                        (
                        codVenta INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                        codCabecera INT (10) NOT NULL,
                        codProducto INT (10) NOT NULL,
                        cantidad VARCHAR(100) NOT NULL,
                        precioUnitario VARCHAR(100) NOT NULL, 
                        condPago VARCHAR(100)NOT NULL
                        
                        
                        )"""
            cursor.execute(sql)
            self.conn.commit()

   
    
    def getVentas(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM venta"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getVenta(self, cod):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM venta WHERE codVenta = %s"""
            cursor.execute(sql,cod)
            result = cursor.fetchone()
            if result:
                return result
    
   

    def deleteVenta(self,cod):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM venta WHERE codVenta = %s"""
            cursor.execute(sql, cod)
            self.conn.commit()
    
    def insertVenta(self,codCabecera,codProducto,cantidad,precio,condPago):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO venta (codCabecera,codProducto,cantidad,precioUnitario,condPago) VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (codCabecera,codProducto,cantidad,precio,condPago))
            self.conn.commit()

    

    

    def ventasDiarias(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%d/%m/%Y"), SUM(df.cantidad * df.precioUnitario) 
                    FROM cabecerafactura cf ,venta df
                    WHERE
                    df.codCabecera = cf.nroFactura 
                    AND cf.activo = '1'
                    GROUP BY date_format(cf.fechaYhora, "%d/%m/%Y")
                   
                    """
                    
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result

    def ventasMensuales(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%M-%Y"), SUM(df.cantidad * df.precioUnitario) 
                    FROM cabecerafactura cf ,venta df
                    WHERE
                    df.codCabecera = cf.nroFactura 
                    AND cf.activo = '1'
                    GROUP BY date_format(cf.fechaYhora, "%M-%Y")
                   
                    """
                    
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result


    def detalleVentas(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%d-%m-%Y/%H:%i"),cf.nroFactura, cc.codCliente, dp.codProducto, df.cantidad, dp.producto, df.precioUnitario, df.cantidad * df.precioUnitario 
                    FROM cabecerafactura cf ,venta df, Product dp, cliente cc 
                    WHERE
                    cf.nroFactura = df.codCabecera
                    AND
                    cc.codCliente = cf.codCliente
                    AND
                    dp.codProducto = df.codProducto
                    AND cf.activo = '1'
                    order by cf.nroFactura               
                     
                    """
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result
    
    def ventaPorFecha(self, fecha):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura, SUM(df.cantidad * df.precioUnitario) 
                    FROM cabecerafactura cf ,venta df 
                    WHERE
                    DATE(cf.fechaYhora) = %s AND
                    cf.nroFactura = df.codCabecera
                    AND cf.activo = '1'
                    GROUP BY date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura
                    order by cf.nroFactura
                    """
            cursor.execute(sql,fecha)
            result = cursor.fetchall()
            if result:
                return result

    def ventaPorFactura(self,nroFactura):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura, cc.codCliente, dp.codProducto, df.cantidad, dp.producto, df.precioUnitario, df.cantidad * df.precioUnitario 
                    FROM cabecerafactura cf ,venta df, Product dp, cliente cc 
                    WHERE
                    cf.nroFactura = df.codCabecera
                    AND
                    cc.codCliente = cf.codCliente
                    AND
                    dp.codProducto = df.codProducto
                    AND 
                    cf.nroFactura = %s
                    AND cf.activo = '1'
                    order by cf.nroFactura               
                     
                    """
            cursor.execute(sql,nroFactura)
            result = cursor.fetchall()
            if result:
                return result

    def imprimirVentas(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%d-%m-%Y/%H:%i"),cf.nroFactura, SUM(df.cantidad * df.precioUnitario) 
                    FROM cabecerafactura cf ,venta df 
                    WHERE
                    DATE(cf.fechaYhora) = CURDATE() AND
                    cf.nroFactura = df.codCabecera
                    AND cf.activo= '1'
                    GROUP BY date_format(cf.fechaYhora, "%d-%m-%Y/%H:%i"),cf.nroFactura
                    order by cf.nroFactura              
                     
                    """
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result

    def detalleFecha(self, fecha):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura, cc.codCliente, dp.codProducto, df.cantidad, dp.producto, df.precioUnitario, df.cantidad * df.precioUnitario 
                    FROM cabecerafactura cf ,venta df, Product dp, cliente cc 
                    WHERE
                    DATE(cf.fechaYhora) = %s 
                    AND
                    cf.nroFactura = df.codCabecera
                    AND
                    cc.codCliente = cf.codCliente
                    AND
                    dp.codProducto = df.codProducto
                    AND 
                    cf.activo = '1'
                    order by cf.nroFactura 
                   
                    """
            cursor.execute(sql,fecha)
            result = cursor.fetchall()
            if result:
                return result
                
    def importeYfecha(self, fecha):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%%d/%%m/%%Y"), SUM(df.cantidad * df.precioUnitario) 
                    FROM cabecerafactura cf ,venta df
                    WHERE
                    DATE(cf.fechaYhora) = %s 
                    AND
                    df.codCabecera = cf.nroFactura 
                    AND
                    cf.activo = '1'
                    GROUP BY date_format(cf.fechaYhora, "%%d/%%m/%%Y")
                   
                    """     
            cursor.execute(sql,fecha)
            result = cursor.fetchall()
            if result:
                return result

    def condPago(self,condPago):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura, SUM(df.cantidad * df.precioUnitario), dd.user_name 
                    FROM cabecerafactura cf ,venta df, User dd
                    WHERE
                    cf.nroFactura = df.codCabecera
                    AND
                    cf.codUsuario = dd.codUsuario
                   
                    AND 
                    df.condPago = %s
                    AND
                    cf.activo = '1'
                    GROUP BY date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura
                    order by cf.nroFactura               
                     
                    """
            cursor.execute(sql,condPago)
            result = cursor.fetchall()
            if result:
                return result
        
    def condPagoTodos(self):
        with self.conn.cursor() as cursor:
            sql ="""SELECT date_format(cf.fechaYhora, "%d-%m-%Y/%H:%i"),cf.nroFactura, SUM(df.cantidad * df.precioUnitario), dd.user_name 
                    FROM cabecerafactura cf ,venta df, User dd
                    WHERE
                    cf.nroFactura = df.codCabecera
                    AND
                    cf.codUsuario = dd.codUsuario
                    AND
                    cf.activo = '1'
                    GROUP BY date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura
                    
                    order by cf.nroFactura               
                     
                    """
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result

    def condPago_2(self,condPago):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura, cc.codCliente, dp.codProducto, df.cantidad, dp.producto, df.precioUnitario, df.cantidad * df.precioUnitario 
                    FROM cabecerafactura cf ,venta df, Product dp, cliente cc 
                    WHERE
                    cf.nroFactura = df.codCabecera
                    AND
                    cc.codCliente = cf.codCliente
                    AND
                    dp.codProducto = df.codProducto
                    AND
                    condPago = %s
                    AND
                    cf.activo = '1'
                    order by cf.nroFactura               
                     
                    """
            cursor.execute(sql,condPago)
            result = cursor.fetchall()
            if result:
                return result
        
    def condPagoTodos_2(self):
        with self.conn.cursor() as cursor:
            sql ="""SELECT date_format(cf.fechaYhora, "%d-%m-%Y/%H:%i"),cf.nroFactura, cc.codCliente, dp.codProducto, df.cantidad, dp.producto, df.precioUnitario, df.cantidad * df.precioUnitario 
                    FROM cabecerafactura cf ,venta df, Product dp, cliente cc 
                    WHERE
                    cf.nroFactura = df.codCabecera
                    AND
                    cc.codCliente = cf.codCliente
                    AND
                    dp.codProducto = df.codProducto
                    AND
                    cf.activo = '1'
                    order by cf.nroFactura               
                     
                    """
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result

    def anular_venta(self,nroFactura):
        with self.conn.cursor() as cursor:
            sql ="""UPDATE  product, venta, cabecerafactura SET product.stock = product.stock + venta.cantidad 
                    WHERE cabecerafactura.nroFactura = venta.codCabecera
                    AND product.codProducto = venta.codProducto 
                    AND  cabecerafactura.nroFactura = %s          
                    """
            cursor.execute(sql,nroFactura)
            self.conn.commit()
    
    

    def listarVentasAnuladas(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%d-%m-%Y/%H:%i"),cf.nroFactura, SUM(df.cantidad * df.precioUnitario), cc.codCliente,dd.user_name 
                    FROM cabecerafactura cf ,venta df, cliente cc, User dd
                    WHERE
                    cf.nroFactura = df.codCabecera
                    AND
                    cc.codCliente = cf.codCliente
                    AND
                    dd.codUsuario = cf.codUsuario
                    AND
                    cf.activo = '0'
                    GROUP BY date_format(cf.fechaYhora, "%d-%m-%Y/%H:%i"),cf.nroFactura
                    order by cf.nroFactura                 
                    """
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result

    def buscarAnulada(self,nroFactura):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura, SUM(df.cantidad * df.precioUnitario), cc.codCliente,cc.nombreCliente  
                    FROM cabecerafactura cf ,venta df, cliente cc
                    WHERE
                    cf.nroFactura = df.codCabecera
                    AND
                    cc.codCliente = cf.codCliente
                    AND
                    cf.nroFactura = %s
                    AND
                    cf.activo = '0'
                    GROUP BY date_format(cf.fechaYhora, "%%d-%%m-%%Y/%%H:%%i"),cf.nroFactura
                    order by cf.nroFactura               
                     
                    """
            cursor.execute(sql,nroFactura)
            result = cursor.fetchall()
            if result:
                return result

    def showDetalleAnulada(self,nroFactura):
        with self.conn.cursor() as cursor:
            sql = """ SELECT  dp.producto, df.cantidad, df.precioUnitario, df.cantidad * df.precioUnitario 
                    FROM cabecerafactura cf ,venta df, Product dp 
                    WHERE
                    cf.nroFactura = df.codCabecera
                    AND
                    dp.codProducto = df.codProducto
                    AND cf.activo = '0'
                    AND cf.nroFactura = %s
                    order by cf.nroFactura             
                     
                    """
            cursor.execute(sql,nroFactura)
            result = cursor.fetchall()
            if result:
                return result

            