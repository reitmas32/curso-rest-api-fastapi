from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola desde FastAPI"}

@app.get("/suma")
def suma(a: int, b: int):
    return {"resultado": a + b}
