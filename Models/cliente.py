class Cliente():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS cliente
                        (
                        codCliente INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        nombreCliente VARCHAR(45) NOT NULL,
                        nroDni INT(10) NOT NULL,
                        fechaAlta VARCHAR(45) NOT NULL,
                        calle VARCHAR (20) NOT NULL, 
                        
                        nroCalle INT(10) NOT NULL,
                        ciudad VARCHAR(45) NOT NULL,
                        codPostal INT(10) NOT NULL,
                        tel INT(20) NOT NULL,
                        email VARCHAR(45) NOT NULL
                        )"""
            cursor.execute(sql)
            self.conn.commit()

    def insertCliente(self,nombreCliente, nroDni, fechaAlta, calle, nroCalle, ciudad, codPostal, tel, email):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO cliente (nombreCliente,nroDni,fechaAlta,calle,nroCalle,ciudad, codPostal, tel,email) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (nombreCliente, nroDni, fechaAlta, calle, nroCalle, ciudad, codPostal, tel, email))
            self.conn.commit()

    def getCliente(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM cliente"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getCliente(self, nroDni):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM cliente WHERE nroDni = %s"""
            cursor.execute(sql,nroDni)
            result = cursor.fetchone()
            if result:
                return result
    
    def updateCliente(self,nombreCliente, nroDni, fechaAlta, calle, nroCalle, ciudad, codPostal, tel, email):
        with self.conn.cursor() as cursor:
            sql = """UPDATE cliente SET nombreCliente =%s, numDni = %s,fechaAlta = %s, calle = %s,nroCalle = %s,ciudad = %s, cosPostal = %s, tel = %s, email= %s WHERE codCliente = %s """
            cursor.execute(sql,(nombreCliente, nroDni, fechaAlta, calle, nroCalle, ciudad, codPostal, tel, email))
            self.conn.commit()

    def deleteCliente(self,nroDni):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM cliente WHERE nroDni = %s"""
            cursor.execute(sql, nroDni)
            self.conn.commit()