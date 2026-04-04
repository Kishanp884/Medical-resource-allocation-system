from fastapi import APIRouter
from models import Alert

router = APIRouter()

alerts = []

@router.post("/alerts")
def create_alert(a: Alert):
    alerts.append(a)
    return {"msg": "Alert created"}

@router.get("/alerts")
def get_alerts():
    return alerts