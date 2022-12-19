"""Modules"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    """Returns Hello World"""
    return "hello world"
