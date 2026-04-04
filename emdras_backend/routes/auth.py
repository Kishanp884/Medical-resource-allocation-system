from fastapi import APIRouter
from models import User

router = APIRouter()

users = []

@router.post("/login")
def login(user: User):
    users.append(user)
    return {"msg": "Login successful"}