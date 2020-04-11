from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")

@app.get("/")
def dashboard(request: Request):
    """
    displays the stocks screener dashboard
    """
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.get("/api/users")
def create_stock():
    """
    creates a stokc and stores it in the database
    """
    return [
        {"name": "Madan Chalal", "email": "madan.ch@gmail.com"},
        {"name": "Joe Blogs", "email": "joe.blogs@apple.com"}
    ]