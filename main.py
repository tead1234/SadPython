from dataclasses import asdict
from typing import Optional

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"da": "hji"}
@app.get('/blog/{id}')
def comments(id: int):
    return {'data': {
        id
    }   }

@app.get('/blog/unpublished'):
def unpublished():
    return {
        'data' : 'all unpublished blogs'
    }