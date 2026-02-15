# 🏋️ Fitness Studio Booking API

## 🚀 Project Overview

This project is a backend API built using **FastAPI** for managing a fictional fitness studio.

The system allows users to:

- Register and authenticate using **JWT**
- Create fitness classes
- View upcoming classes
- Book available classes
- View their personal bookings

The application follows clean architecture principles with proper authentication, validation, and business logic handling.

---

## 🛠 Tech Stack

- **Language:** Python 3  
- **Framework:** FastAPI  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **Authentication:** JWT (JSON Web Token)  
- **Password Hashing:** Passlib (bcrypt)  
- **API Docs:** Swagger UI (`/docs`)  

---

## 🏗 Project Structure

```bash
starlabs-booking-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── dependencies.py
│   └── routers/
│       ├── users.py
│       ├── classes.py
│       └── bookings.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

The project is modular and separates:

- **Models** (database layer)  
- **Schemas** (validation layer)  
- **Routers** (API layer)  
- **Authentication logic**  
- **Database configuration**

---

## 🔐 Authentication

- JWT-based authentication  
- Passwords securely hashed using bcrypt  
- Token expiration enabled  
- Protected routes require:

```http
Authorization: Bearer <token>
```

### 🔒 Protected Endpoints

- `POST /classes`
- `POST /book`
- `GET /bookings`

---

## 📦 API Endpoints

### 👤 Authentication

| Method | Endpoint  | Description                     |
|--------|-----------|--------------------------------|
| POST   | `/signup` | Register a new user            |
| POST   | `/login`  | Authenticate user & return JWT |

### 🧘 Classes

| Method | Endpoint    | Description                           |
|--------|------------|---------------------------------------|
| POST   | `/classes` | Create a new class (Auth required)    |
| GET    | `/classes` | View upcoming classes                 |

### 📅 Bookings

| Method | Endpoint     | Description                               |
|--------|-------------|-------------------------------------------|
| POST   | `/book`     | Book a class (Auth required)              |
| GET    | `/bookings` | View logged-in user’s bookings            |

---

## 🧠 Business Logic Implemented

- ✔ Prevents overbooking  
- ✔ Prevents duplicate bookings  
- ✔ Prevents booking past classes  
- ✔ Deducts available slots upon successful booking  
- ✔ Returns appropriate HTTP status codes  
- ✔ Validates required fields  

---

## ⏰ Timezone Handling

- All class times are stored in **IST (Indian Standard Time)**  
- ISO 8601 datetime format is used for API communication  
- Past classes cannot be booked  

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <your_repo_url>
cd starlabs-booking-api
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

### 6. Access API Documentation

Open in your browser:

```
http://127.0.0.1:8000/docs
```

---

## 🌱 Sample Input Data

### 👤 Sample User

```json
POST /signup
{
  "name": "User",
  "email": "user@example.com",
  "password": "user@123"
}
```

### 🧘 Sample Fitness Class

```json
POST /classes
{
  "name": "HIIT Blast",
  "date_time": "2026-06-20T09:00:00",
  "instructor": "Jane Smith",
  "available_slots": 15
}
```

---

## 🔧 API Usage Examples (cURL)

### Signup

```bash
curl -X POST http://127.0.0.1:8000/signup \
-H "Content-Type: application/json" \
-d "{\"name\":\"User\",\"email\":\"user@example.com\",\"password\":\"user@123\"}"
```

### Login

```bash
curl -X POST http://127.0.0.1:8000/login \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "username=user@example.com&password=user@123"
```

#### Login Response

```json
{
  "access_token": "your_token_here",
  "token_type": "bearer"
}
```

### Create Class (Authenticated)

```bash
curl -X POST http://127.0.0.1:8000/classes \
-H "Authorization: Bearer your_token_here" \
-H "Content-Type: application/json" \
-d "{\"name\":\"Yoga Flow\",\"date_time\":\"2026-06-15T10:00:00\",\"instructor\":\"John Doe\",\"available_slots\":20}"
```

### Book Class

```bash
curl -X POST http://127.0.0.1:8000/book \
-H "Authorization: Bearer your_token_here" \
-H "Content-Type: application/json" \
-d "{\"class_id\":1}"
```

### View Bookings

```bash
curl -X GET http://127.0.0.1:8000/bookings \
-H "Authorization: Bearer your_token_here"
```

---

## 📌 Additional Notes

- Swagger documentation available at `/docs`
- SQLite used for development
- Easily extendable to PostgreSQL
- Modular router-based structure
- Designed for scalability and maintainability

---

## 👩‍💻 Author

**Harmeen Safoora**  
Backend Developer Intern Applicant
