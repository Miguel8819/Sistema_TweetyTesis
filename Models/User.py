class User():

    def __init__(self,conn):
        self.conn = conn
        with self.conn.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS user
                        (user_name VARCHAR(100) NOT NULL,
                        password VARCHAR(100) NOT NULL,
                        rol VARCHAR(30) NOT NULL
                        )
                        """
            cursor.execute(sql)
            self.conn.commit()
    def getUser1(self, user):
        with self.conn.cursor() as cursor:
            sql = """SELECT user_name FROM user WHERE user_name = %s"""
            cursor.execute(sql, (user))
            result = cursor.fetchone()
            return result
    
    def getUser(self, user, password):
        with self.conn.cursor() as cursor:
            sql = """SELECT user_name FROM user WHERE user_name = %s AND password = %s"""
            cursor.execute(sql, (user,password))
            result = cursor.fetchone()
            return result

    def updatePassword(self, user, password, newPass):
        with self.conn.cursor() as cursor: 
            sql = """UPDATE user SET password = '{}' WHERE user_name = '{}' AND password = '{}'""".format(newPass, user, password)
            cursor.execute(sql)
            self.conn.commit() 
            if cursor.rowcount > 0:
                success = True
                return success
            else:
                failure = False
                return failure

    def registrarUsuario(self,user, password, rol):
         with self.conn.cursor() as cursor:          
            sql = """INSERT INTO user (user_name, password, rol) VALUES (%s,%s,%s)"""
            cursor.execute(sql, (user, password, rol))
            self.conn.commit()
            
            
                