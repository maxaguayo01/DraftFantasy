from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from info.models import User

app = FastAPI()

class RegisterModel(BaseModel):
    email: str
    code: str

@app.post("/register")
def register_user(data: RegisterModel):
    User(email=data.email, code=data.code).save()
    return {"status": "ok"}

@app.get("/login")
def login_user(email: str, code: str):
    if not User.authenticate(email, code):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"status": "ok"}
