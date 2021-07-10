from main import app, db
from fastapi import HTTPException

@app.get('/store/average/{column}')
def get(column: str):
    db_df = db._get_dataframe()
    return {'data': db_df[column].mean()}
