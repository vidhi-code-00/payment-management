from fastapi import FastAPI
from app.routes.auth import router as authrouter
from app.core.database import Base, engine
from app.routes.transaction_api import router as transactionrouter

app = FastAPI(title="payment management system")
Base.metadata.create_all(bind=engine)

app.include_router(authrouter)
app.include_router(transactionrouter)

@app.get("/test")
def test():
    return {
      "Payment Server started successfuly"
    }
