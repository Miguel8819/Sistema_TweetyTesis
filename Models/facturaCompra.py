class FacturaCompra():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS facturaCompra
                        (
                        codFactCompra INT(10) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
                        nroFacturaCompra INT (10) NOT NULL,
                        codProducto INT (10) NOT NULL,
                        cantidad VARCHAR(100) NOT NULL,
                        precioUnitario VARCHAR(100) NOT NULL 
                        fechaIngreso VARCHAR (10) NOT NULL,
                        fechaEmision VARCHAR (10) NOT NULL
                        )"""
            cursor.execute(sql)
            self.conn.commit()

    def insertFactCompra(self,nroFactCompra,codProducto,cantidad,precio,fechaIngreso,fechaEmision):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO facturaCompra (nroFacturaCompra,codProducto,cantidad,precioUnitario,fechaIngreso,fechaEmision) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (nroFactCompra,codProducto,cantidad,precio,fechaIngreso,fechaEmision))
            self.conn.commit()