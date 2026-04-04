from fastapi import APIRouter
from models import IVData

router = APIRouter()

iv_data = []

@router.post("/iv")
def add_iv(data: IVData):
    iv_data.append(data)
    return {"msg": "IV data added"}

@router.get("/iv")
def get_iv():
    return iv_data