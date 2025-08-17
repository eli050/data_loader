import os
import pymysql

class DataLoader:
    def __init__(self):
        self.host = os.getenv("DB_HOST", "mysql")
        self.port = int(os.getenv("DB_PORT", "3306"))
        self.user = os.getenv("DB_USER", "appuser")
        self.password = os.getenv("DB_PASSWORD", "apppass")
        self.database = os.getenv("DB_NAME", "appdb")

    def get_all(self):
        conn = pymysql.connect(
            host=self.host, port=self.port,
            user=self.user, password=self.password,
            database=self.database, cursorclass=pymysql.cursors.DictCursor
        )
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT id, first_name, last_name FROM data ORDER BY id")
                return cur.fetchall()
        finally:
            conn.close()
