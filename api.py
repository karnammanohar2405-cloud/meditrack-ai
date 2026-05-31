from fastapi import FastAPI
from data.database import fetch_reports, fetch_hospitals, fetch_medicines

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Health API is running"}

@app.get("/reports")
def get_reports():
    return fetch_reports()

@app.get("/hospitals")
def get_hospitals():
    return fetch_hospitals()

@app.get("/medicines")
def get_medicines():
    return fetch_medicines()