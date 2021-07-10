import uvicorn
from fastapi import FastAPI
from configuration.config import DB_CSV_PATH
from db.store_csv_database import StoreCSVDatabase

app = FastAPI()
db = StoreCSVDatabase(DB_CSV_PATH)
from views import store_api
from views import store_statistics_api

if __name__ == "__main__":

    # uvicorn.run("app:app", reload=True)
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000)
