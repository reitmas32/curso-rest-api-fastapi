from fastapi import FastAPI
import httpx  # Cliente HTTP asíncrono

app = FastAPI()

@app.get("/")
async def get_ip():
    response = await httpx.get("https://httpbin.org/ip")
    return response.json()
