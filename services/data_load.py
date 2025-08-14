from fastapi import FastAPI
import uvicorn
from services.my_sql_data import MySqlData

app = FastAPI()


@app.get("/data")
def get_data():
    query = "SELECT * FROM data"
    with MySqlData.get_connection() as conn:
        if conn:
            with conn.cursor() as cmd:
                cmd.execute(query)
                return cmd.fetchall()
        else:
            print("Failed to connect to the database.")


if __name__ == '__main__':
    uvicorn.run(app)