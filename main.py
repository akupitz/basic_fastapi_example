import uvicorn

from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# if __name__ == "__main__":
# localhost/docs will give us the swagger
# localhost/redoc will give us the swagger validations


if __name__ == "__main__":
    # uvicorn.run("app:app", reload=True)
    uvicorn.run("store_api:app", host="127.0.0.1", port=8000)
