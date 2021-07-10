from main import app, db

from fastapi import HTTPException
# from fastapi import FastAPI, HTTPException
from db.store_csv_database import StoreCSVDatabase
from store.models import Product
from configuration.config import DB_CSV_PATH

# app = FastAPI()
# db = StoreCSVDatabase(DB_CSV_PATH)


# localhost/docs will give us the swagger
# localhost/redoc will give us the swagger validations
@app.get('/')
def home():
    return "Store home page, go to /docs"


@app.get('/store/get/{product_name}')
def get(product_name: str):
    product_info = db.get(product_name)
    if product_info is None:
        raise HTTPException(status_code=400, detail="product name is invalid")
    else:
        return {'data': product_info}


@app.get('/store/get_all')
def get_all():
    all_products_info = db.get_all()
    return {'data': all_products_info}


@app.post('/store/insert')
def insert(product: Product):
    if db.get(product.name) is not None:
        raise HTTPException(status_code=400, detail="product can't be inserted since it already exists")
    db.insert(product)
    return {'data': f"Product {product.name} was inserted successfully"}


@app.put('/store/update')
def update(product: Product):
    if db.get(product.name) is None:
        raise HTTPException(status_code=400, detail="product can't be updated since it does not exist")
    db.update(product)
    return {"data": f"Product {product.name} was updated successfully"}


@app.delete('/store/remove/{product_name}')
def remove(product_name: str):
    if db.get(product_name) is None:
        raise HTTPException(status_code=400, detail="product can't be removed since it does not exist")
    db.remove(product_name)
    return {'data': f"Product {product_name} was removed successfully"}