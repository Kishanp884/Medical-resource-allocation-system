from fastapi import APIRouter
from models import Organ

router = APIRouter()

organs = []

@router.post("/organs")
def add_organ(o: Organ):
    organs.append(o)
    return {"msg": "Organ added"}

@router.get("/organs")
def get_organs():
    return organs