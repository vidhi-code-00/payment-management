from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.dashboard import Dashboard

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def get_dashboard(db: Session = Depends(get_db)):

    dashboard = db.query(Dashboard).first()

    if not dashboard:
        dashboard = Dashboard(
            total_users=0,
            total_transactions=0,
            total_amount=0
        )

        db.add(dashboard)
        db.commit()
        db.refresh(dashboard)

    return {
        "total_users": dashboard.total_users,
        "total_transactions": dashboard.total_transactions,
        "total_amount": dashboard.total_amount
    }