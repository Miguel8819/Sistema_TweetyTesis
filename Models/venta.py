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
                        precioUnitario VARCHAR(100) NOT NULL 
                        
                        
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
    
    def insertVenta(self,codCabecera,codProducto,cantidad,precio):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO venta (codCabecera,codProducto,cantidad,precioUnitario) VALUES (%s,%s,%s,%s)"""
            cursor.execute(sql, (codCabecera,codProducto,cantidad,precio))
            self.conn.commit()

    

    def ventasDiarias(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT date_format(cf.fechaYhora, "%d/%m/%Y"), SUM(df.cantidad * df.precioUnitario) 
                    FROM cabecerafactura cf ,venta df
                    WHERE
                    df.codCabecera = cf.nroFactura 
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
                    order by cf.nroFactura               
                     
                    """
            cursor.execute(sql)
            result = cursor.fetchall()
            if result:
                return result
    
    def ventaPorFecha(self, fecha):
        with self.conn.cursor() as cursor:
            sql = """"SELECT date_format(cf.fechaYhora, "%%d-%%m-%%Y"), SUM(df.cantidad * df.precioUnitario) 
                    FROM cabecerafactura cf ,venta df
                    WHERE
                    cf.fechaYhora = %s
                    AND
                    df.codCabecera = cf.nroFactura 
                    GROUP BY date_format(cf.fechaYhora, "%%d-%%m-%%Y")
                   
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
                    order by cf.nroFactura               
                     
                    """
            cursor.execute(sql,nroFactura)
            result = cursor.fetchall()
            if result:
                return result
            