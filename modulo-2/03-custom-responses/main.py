from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel

app = FastAPI()


# Modelo Pydantic
class User(BaseModel):
    name: str
    email: str


@app.get("/custom-json-response")
def custom_json_response():
    content = {"message": "This is a custom response"}
    headers = {"X-App-Version": "1.0.0", "X-Powered-By": "FastAPI"}
    return JSONResponse(content=content, status_code=202, headers=headers)


# (text/plain)
@app.get("/plain-text")
def plain_text_response():
    return PlainTextResponse("Hello, this is plain text", headers={"X-Custom-Header": "plain-response"})


# (xml)
@app.get("/custom-xml")
def custom_xml_response():
    content = "<user><name>Rafa</name><email>rafa@example.com</email></user>"
    return Response(content=content, media_type="application/xml", headers={"X-Format": "XML"})


# (json)
@app.post("/create-user", response_model=User)
def create_user(user: User, response: Response):
    response.headers["X-User-Created"] = "true"
    response.headers["X-Custom-ID"] = "abc-123"
    return user

