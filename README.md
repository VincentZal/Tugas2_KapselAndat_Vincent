# TUGAS 2 KAPITA SELEKTA ANALITIKA DATA
CRUD API untuk Users Module dengan FastAPI

## Cara menggunakan :
 1. Buat virtual environment:
    py -m venv venv
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
    
