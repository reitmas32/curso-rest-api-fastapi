from fastapi import FastAPI, Header, Response
from typing import Annotated

app = FastAPI()


# ✅ Leer headers personalizados enviados por el cliente
@app.get("/read-headers")
def read_headers(
    user_agent: Annotated[str | None, Header()] = None,
    x_token: Annotated[str | None, Header()] = None,
    x_request_id: Annotated[str | None, Header()] = None
):
    return {
        "user_agent": user_agent,
        "x_token": x_token,
        "x_request_id": x_request_id
    }


# ✅ Enviar headers personalizados en la respuesta
@app.get("/send-custom-headers")
def send_custom_headers(response: Response):
    response.headers["X-App-Version"] = "2.5.1"
    response.headers["X-Powered-By"] = "FastAPI"
    response.headers["X-Developer"] = "Rafa Zamora"
    return {"message": "Headers sent!"}


# ✅ Combinar ambos: leer y responder con headers
@app.get("/echo-header")
def echo_header(
    x_echo: Annotated[str | None, Header()] = None,
    response: Response = None
):
    if x_echo:
        response.headers["X-Echoed-Back"] = x_echo
    return {"received": x_echo}
