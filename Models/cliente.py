class Cliente():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS cliente
                        (
                        codCliente INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        nroDni VARCHAR(10) NOT NULL,
                        nombreCliente VARCHAR(45) NOT NULL,
                        fechaAlta VARCHAR(45) NOT NULL,
                        calle VARCHAR (35) NOT NULL, 
                        nroCalle VARCHAR(10) NOT NULL,
                        ciudad VARCHAR(45) NOT NULL,
                        codPostal VARCHAR(10) NOT NULL,
                        tel VARCHAR(20) NOT NULL,
                        email VARCHAR(45) NOT NULL,
                        activo BOOLEAN NOT NULL,
                        fechaBaja VARCHAR(45) NOT NULL,
                        codUsuario INT(10) NOT NULL
                        )"""
            cursor.execute(sql)
            self.conn.commit()

    def insertCliente(self,nombreCliente, nroDni, fechaAlta, calle, nroCalle, ciudad, codPostal, tel, email,usuario):
        with self.conn.cursor() as cursor:
            activo = 1
            sql = """INSERT INTO cliente (nombreCliente,nroDni,fechaAlta,calle,nroCalle,ciudad, codPostal, tel,email,activo,codUsuario) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (nombreCliente, nroDni, fechaAlta, calle, nroCalle, ciudad, codPostal, tel, email, activo,usuario))
            self.conn.commit()

    def getClientes(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM cliente"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getCliente(self, nroDni, estado):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM cliente WHERE nroDni = %s AND activo = %s"""
            cursor.execute(sql,(nroDni,estado))
            result = cursor.fetchone()
            if result:
                return result
    
    def updateCliente(self,nombreCliente, nroDni,  calle, nroCalle, ciudad, codPostal, tel, email):
        with self.conn.cursor() as cursor:
            sql = """UPDATE cliente SET nombreCliente =%s, calle = %s,nroCalle = %s,ciudad = %s, codPostal = %s, tel = %s, email= %s WHERE nroDni = %s """
            cursor.execute(sql,(nombreCliente, calle, nroCalle, ciudad, codPostal, tel, email,nroDni))
            self.conn.commit()

    def deleteCliente(self,nroDni):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM cliente WHERE nroDni = %s"""
            cursor.execute(sql, nroDni)
            self.conn.commit()

    def bajaCliente(self,nroDni,fechaBaja,usuario):
        with self.conn.cursor() as cursor:
            sql = """UPDATE cliente SET activo = "0", fechaBaja = %s, codUsuario = %s WHERE nroDni = %s"""
            cursor.execute(sql, (fechaBaja,usuario,nroDni))
            self.conn.commit()

    def altaCliente(self,nroDni,fechaAlta):
        with self.conn.cursor() as cursor:
            sql = """UPDATE cliente SET activo = "1", fechaAlta= %s WHERE nroDni = %s"""
            cursor.execute(sql,(fechaAlta, nroDni))
            self.conn.commit()

    def getClientesActivos(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT  c.codCliente, c.nroDni, c.nombreCliente, c.fechaAlta, c.calle, c.nroCalle, c.ciudad, c.codPostal, c.tel, c.email, c.codUsuario 
            FROM cliente c
            WHERE activo = '1' 
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    def getClientesBaja(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT c.codCliente, c.nroDni, c.nombreCliente, c.fechaAlta, c.fechaBaja, c.tel, c.email, c.codUsuario 
            FROM cliente c 
            WHERE activo = '0' 
            """
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
