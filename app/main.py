from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import Base, engine

# routers
from app.routes.auth import router as auth_router
from app.routes.transaction_api import router as transaction_router

app = FastAPI()

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- DB INIT ----------------
try:
    Base.metadata.create_all(bind=engine)
    print("✅ Database connected & tables created")
except Exception as e:
    print("❌ DB Error:", e)

# ---------------- ROUTES ----------------
app.include_router(auth_router, prefix="/api/auth")
app.include_router(transaction_router, prefix="/api/transactions")

# ---------------- TEST ROUTES ----------------
@app.get("/")
def home():
    return {"msg": "FastAPI running"}

@app.get("/test")
def test():
    return {"msg": "server working fine"}