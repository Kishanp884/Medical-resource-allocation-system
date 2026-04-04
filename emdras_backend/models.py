from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    role: str

class Resource(BaseModel):
    hospital: str
    beds: int
    ventilators: int
    status: str

class Organ(BaseModel):
    organ_id: str
    type: str
    blood_group: str
    location: str
    status: str

class IVData(BaseModel):
    patient_id: str
    flow_rate: float
    volume: float

class Alert(BaseModel):
    type: str
    severity: str
    location: str