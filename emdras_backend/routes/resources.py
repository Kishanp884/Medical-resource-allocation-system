from fastapi import APIRouter
from models import Resource

router = APIRouter()

resources = []

@router.post("/resources")
def add_resource(r: Resource):
    resources.append(r)
    return {"msg": "Resource added"}

@router.get("/resources")
def get_resources():
    return resources