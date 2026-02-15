from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
import pytz

from .. import models, schemas
from ..dependencies import get_db
from ..auth import get_current_user

router = APIRouter()

# CREATE CLASS (Protected)
@router.post("/classes", response_model=schemas.ClassResponse)
def create_class(
    fitness_class: schemas.ClassCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    # Convert incoming datetime to IST
    ist = pytz.timezone("Asia/Kolkata")
    class_time = fitness_class.date_time.astimezone(ist)

    new_class = models.FitnessClass(
    name=fitness_class.name,
    date_time=class_time,
        instructor=fitness_class.instructor,
        available_slots=fitness_class.available_slots
    )

    db.add(new_class)
    db.commit()
    db.refresh(new_class)

    return new_class

# GET ALL UPCOMING CLASSES
@router.get("/classes", response_model=list[schemas.ClassResponse])
def get_classes(db: Session = Depends(get_db)):

    now = datetime.utcnow()

    classes = db.query(models.FitnessClass).filter(
        models.FitnessClass.date_time > now
    ).all()

    return classes
