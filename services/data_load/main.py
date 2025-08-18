from fastapi import FastAPI
import pymysql
from pymysql import cursors
import os


app = FastAPI()

# === ENV ===
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_SERVICE_HOST", "mysql")
MYSQL_PORT = os.getenv("MYSQL_SERVICE_PORT", "3306")
MYSQL_DB = os.getenv("MYSQL_DATABASE")

def get_db_connection():
    return pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        cursorclass=cursors.DictCursor
    )


@app.get("/")
def root():
    return {"message": "FastAPI + MySQL is running 🎉"}

@app.get("/data")
def get_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

