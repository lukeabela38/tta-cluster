import randfacts
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"text": "Hello World"}

@app.get("/health")
def read_health():
    return 200

@app.get("/random")
def read_random():
    text = randfacts.get_fact()
    return {"random": text}