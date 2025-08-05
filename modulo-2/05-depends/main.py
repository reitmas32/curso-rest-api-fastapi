from fastapi import FastAPI, Depends, Header, HTTPException, status, Request

app = FastAPI()

# Valor de la API Key esperada
API_KEY = "mi_clave_supersecreta"
API_KEY_NAME = "X-API-Key"


# ✅ Dependencia que valida la API Key
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )


# 🔐 Ruta protegida usando Depends()
@app.get("/secure-data", dependencies=[Depends(verify_api_key)])
def secure_data():
    return {"message": "¡Acceso autorizado a los datos protegidos!"}


# 🌐 Ruta pública
@app.get("/public")
def public_data():
    return {"message": "Este endpoint es público"}

# ✅ Dependencia que extrae y retorna la IP del cliente
def get_client_ip(request: Request) -> str:
    client_ip = request.client.host
    return client_ip


# 🧪 Endpoint que recibe la IP como parámetro inyectado por Depends
@app.get("/whoami")
def who_am_i(client_ip: str = Depends(get_client_ip)):
    return {"your_ip": client_ip}
