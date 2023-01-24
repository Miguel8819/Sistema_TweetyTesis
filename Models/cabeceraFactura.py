class CabeceraFactura():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS cabeceraFactura
                        (
                        nroFactura INT(100) NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        fechaYhora DATETIME(6) NOT NULL,
                        codCliente INT(100) NOT NULL,
                        activo BOOLEAN NOT NULL,
                        motivoAnulacion VARCHAR(1000) NOT NULL,
                        codUsuario INT(11) NOT NULL
                        
                        )"""
            cursor.execute(sql)
            self.conn.commit()

   
    
    def getCabeceras(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM nroFactura"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getNroFactura(self, nroFactura):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM cabeceraFactura WHERE nroFactura = %s"""
            cursor.execute(sql,nroFactura)
            result = cursor.fetchone()
            if result:
                return result
    

    def deleteNroFactura(self,nroFactura):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM nroFactura WHERE nroFactura = %s"""
            cursor.execute(sql, nroFactura)
            self.conn.commit()
    
    def insertCabeceraFactura(self,fecha,codCliente,usuario):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO cabeceraFactura (fechaYhora,codCliente,activo,codUsuario) VALUES (%s,%s,'1',%s)"""
            cursor.execute(sql, (fecha,codCliente,usuario))
            id = cursor.lastrowid
            self.conn.commit()
            return id

    def insertMotivo(self,motivo,nroFactura):
        with self.conn.cursor() as cursor:         
            sql = """UPDATE cabeceraFactura SET motivoAnulacion = %s, activo = '0'
            WHERE cabecerafactura.nroFactura = %s
            """
            cursor.execute(sql,(motivo,nroFactura))
            self.conn.commit()

    

            