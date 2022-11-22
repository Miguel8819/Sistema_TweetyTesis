class Proveedor():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS proveedor
                        (codProveedor INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        nombreProveedor VARCHAR(45) NOT NULL,
                        nombreFactura VARCHAR(45) NOT NULL,
                        fechaAlta VARCHAR (10) NOT NULL, 
                        calle VARCHAR(45) NOT NULL,
                        numeroCalle VARCHAR(45) NOT NULL,
                        ciudad VARCHAR(45) NOT NULL,
                        codPostal INT(45) NOT NULL,
                        celular VARCHAR(45) NOT NULL,
                        email VARCHAR(45) NOT NULL,
                        pagWeb VARCHAR(45) NOT NULL)"""
            cursor.execute(sql)
            self.conn.commit()

    def insertProveedor(self,nombreProveedor,nombreFactura,fechaAlta,calle,numeroCalle,ciudad,codPostal,celular,email,pagWeb):
        with self.conn.cursor() as cursor:
            activo= 1
            sql = """INSERT INTO proveedor (nombreProveedor,nombreFactura,fechaAlta,calle,numeroCalle,ciudad,codPostal,celular,email,pagWeb,activo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (nombreProveedor,nombreFactura,fechaAlta,calle,numeroCalle,ciudad,codPostal,celular,email,pagWeb,activo))
            self.conn.commit()

    def getProveedor(self, nombreProveedor, estado):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM proveedor WHERE nombreProveedor = %s AND activo = %s"""
            cursor.execute(sql, (nombreProveedor, estado))
            result = cursor.fetchone()
            if result:
                return result
                
    def autoComplete(self):
        with self.conn.cursor as cursor:
            sql ="""SELECT nombreProveedor FROM proveedor WHERE nombreProveedor LIKE = %s"""
            cursor.execute(sql)
            return cursor.fetchall()


