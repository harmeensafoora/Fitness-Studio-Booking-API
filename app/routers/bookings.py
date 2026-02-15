from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from .. import models, schemas
from ..dependencies import get_db
from ..auth import get_current_user

router = APIRouter()


# =========================
# BOOK A CLASS (Protected)
# =========================
@router.post("/book", response_model=schemas.BookingResponse)
def book_class(
    booking: schemas.BookingCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    fitness_class = db.query(models.FitnessClass).filter(
        models.FitnessClass.id == booking.class_id
    ).first()

    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")

    # Prevent booking past classes
    if fitness_class.date_time < datetime.utcnow():

        raise HTTPException(status_code=400, detail="Cannot book past classes")

    # Prevent overbooking
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available")

    # Prevent duplicate booking
    existing_booking = db.query(models.Booking).filter(
        models.Booking.user_id == current_user.id,
        models.Booking.class_id == booking.class_id
    ).first()

    if existing_booking:
        raise HTTPException(status_code=400, detail="Already booked this class")

    # Create booking
    new_booking = models.Booking(
        user_id=current_user.id,
        class_id=booking.class_id
    )

    fitness_class.available_slots -= 1

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return new_booking


# =========================
# VIEW MY BOOKINGS (Protected)
# =========================
@router.get("/bookings", response_model=list[schemas.BookingResponse])
def get_my_bookings(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):

    bookings = db.query(models.Booking).filter(
        models.Booking.user_id == current_user.id
    ).all()

    return bookings
