import pymysql

def connection():
    conn = pymysql.connect(
        host="localhost", port=3306, user="root",
        password="", db="st"
    )
    print('Database is Connected!')
    return conn