from fastapi import FastAPI
from .database import engine, Base
from .routers import users
from .routers import classes
from .routers import bookings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(classes.router)
app.include_router(bookings.router)

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Fitness Booking API running"}
