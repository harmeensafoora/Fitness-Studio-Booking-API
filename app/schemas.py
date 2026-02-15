from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True #allows FastAPI to convert SQLAlchemy object → Pydantic response

class ClassCreate(BaseModel):
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

class ClassResponse(BaseModel):
    id: int
    name: str
    date_time: datetime
    instructor: str
    available_slots: int

    class Config:
        orm_mode = True

class BookingCreate(BaseModel):
    class_id: int

class BookingResponse(BaseModel):
    id: int
    class_id: int
    user_id: int

    class Config:
        orm_mode = True
