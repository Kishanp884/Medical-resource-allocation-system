from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routes import auth, resources, organs, iv, alerts, analytics

app = FastAPI()

# Allow frontend app (Flask or other) to call this backend across ports
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5000", "http://localhost:5000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(resources.router)
app.include_router(organs.router)
app.include_router(iv.router)
app.include_router(alerts.router)
app.include_router(analytics.router)

@app.get("/")
def home():
    return {"message": "EMDRAS Backend Running"}