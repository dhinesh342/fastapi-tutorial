from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index():
    return("Hi User")

@app.get("/about")
def about():
    return {"data":"About Page"}