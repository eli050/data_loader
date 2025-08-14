from fastapi import FastAPI

from services.my_sql_data import MySqlData

app = FastAPI()


@app.get("/data")
def get_data():
    query = "SELECT * FROM data"
    with MySqlData.get_connection() as conn:
        if conn and conn.is_connected():
            with conn.cursor(dictionary=True) as cmd:
                cmd.execute(query)
                return cmd.fetchall()
        else:
            print("Failed to connect to the database.")