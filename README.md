# TUGAS 2 KAPITA SELEKTA ANALITIKA DATA
CRUD API untuk Users Module dengan FastAPI

## Cara menggunakan :
 1. Buat virtual environment:
    py -m venv venv <br>
    venv\Scripts\activate
 2. Install dependencies:
    pip install -r requirements.txt
 3. jalankan server:
    ## Endpoint
- POST /users → create user
- GET /users → get all users (admin only)
- GET /users/{id} → get user by id (admin or self)
- PUT /users/{id} → update user (admin only)
- DELETE /users/{id} → delete user (admin only)

## Testing
Jalankan unit test: 
py -m pytest

Jalankan server : py -m uvicorn app.main:app --reload
    
## Dokumentasi API

Setelah server dijalankan, dokumentasi interaktif API bisa diakses di:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Gambar
![Swagger UI](images/users%20crud%20api.jpg)
![ReDoc](images/users%20crud%20api2.jpg)



