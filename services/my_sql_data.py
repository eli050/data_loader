import pymysql
from pymysql.cursors import DictCursor

class MySqlData:
    @staticmethod
    def get_connection():
        try:
            return pymysql.connect(
                                user = 'root',
                                host='mysql',
                                database='sampledb',
                                port = 3306,
                                password="h04Ic7fRfwbPbigk",
                                cursorclass= DictCursor)
        except (Exception, IOError) as arr:
            print(arr)
            return None


