class Product():
    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS product
                        (
                        codProducto INT(8) NOT NULL AUTO_INCREMENT PRIMARY KEY,    
                        CodigoDeBarras VARCHAR(45) NOT NULL,
                        
                        producto VARCHAR(45) NOT NULL,
                        categoria VARCHAR(45) NOT NULL,
                        subCategoria VARCHAR(45) NOT NULL,
                        marca VARCHAR(45) NOT NULL,
                        tipoUnidad VARCHAR(45) NOT NULL,
                        unidadDeMedida VARCHAR(45) NOT NULL,
                        
                        cant_min_stock VARCHAR(45) NOT NULL,
                        PuntoDePedido VARCHAR(45) NOT NULL,
                        CostoDeCompra VARCHAR(45) NOT NULL,
                        PrecioDeVenta VARCHAR(45) NOT NULL)"""
            cursor.execute(sql)
            self.conn.commit()
    
    def getProducts(self):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM product"""
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    
    def getProduct(self, CodigoDeBarras):
        with self.conn.cursor() as cursor:
            sql = """SELECT * FROM product WHERE CodigoDeBarras = %s"""
            cursor.execute(sql,CodigoDeBarras)
            result = cursor.fetchone()
            if result:
                return result
    
    def updateProduct(self,cod,CodigoDeBarras,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
        with self.conn.cursor() as cursor:
            sql = """UPDATE product SET CodigoDeBarras = %s  producto = %s,categoria = %s,subCategoria = %s,marca = %s,tipoUnidad = %s,UnidadDeMedida = %s,cant_min_stock = %s,PuntoDePedido = %s,CostoDeCompra = %s,PrecioDeVenta = %s WHERE codProducto = %s """
            cursor.execute(sql,(cod,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta,CodigoDeBarras))
            self.conn.commit()

    def deleteProduct(self,CodigoDeBarras):
        with self.conn.cursor() as cursor:
            sql = """DELETE FROM product WHERE CodigoDeBarras = %s"""
            cursor.execute(sql, CodigoDeBarras)
            self.conn.commit()
    
    def insertProduct(self,CodigoDeBarras,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
        with self.conn.cursor() as cursor:
            sql = """INSERT INTO product (CodigoDeBarras,producto,categoria,subCategoria,marca,tipoUnidad,UnidadDeMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql, (CodigoDeBarras,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta))
            self.conn.commit()
            
    # def modificarProduct (self,CodigoDeBarras,cod,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta):
    #     with self.conn.cursor() as cursor:
    #         sql = """UPDATE product SET codProducto =%s, producto = %s,categoria = %s,subCategoria = %s,marca = %s,tipoUnidad = %s,UnidadDeMedida = %s,cant_min_stock = %s,PuntoDePedido = %s,CostoDeCompra = %s,PrecioDeVenta = %s WHERE CodigoDeBarras = %s """
    #         cursor.execute(sql,(CodigoDeBarras,cod,producto,categoria,subCategoria,marca, tipoUnidad,unidadMedida,cant_min_stock,PuntoDePedido,CostoDeCompra,PrecioDeVenta))
    #         self.conn.commit()