import mysql.connector
from mysql.connector import connection

class MySqlData:
    @staticmethod
    def get_connection():
        try:
            return connection.MySQLConnection(
                                user = 'root',
                                host='localhost',
                                database='data_project',
                                port = 3306)
        except (mysql.connector.Error, IOError) as arr:
            print(arr)
            return None


