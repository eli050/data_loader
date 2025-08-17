from fastapi import FastAPI
from .dal import DataLoader

app = FastAPI()
dal = DataLoader()

@app.get("/data")
def read_data():
    return dal.get_all()
