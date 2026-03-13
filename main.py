from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Render!"}

@app.get("/add")
def add(q: str):
    return {"received": q}
