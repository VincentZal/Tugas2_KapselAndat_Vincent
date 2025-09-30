from fastapi import APIRouter, HTTPException, status
from app.models import User
from app.database import users_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    users_db.append(user.dict())
    return user

@router.get("/")
def get_all_users(role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can view all users")
    return users_db

@router.get("/{user_id}")
def get_user(user_id: str, role: str, requester_id: str = None):
    for user in users_db:
        if user["id"] == user_id:
            if role == "admin" or requester_id == user_id:
                return user
            raise HTTPException(status_code=403, detail="Access denied")
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/{user_id}")
def update_user(user_id: str, updated: User, role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can update users")
    for i, user in enumerate(users_db):
        if user["id"] == user_id:
            users_db[i] = updated.dict()
            return updated
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
def delete_user(user_id: str, role: str):
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can delete users")
    for i, user in enumerate(users_db):
        if user["id"] == user_id:
            del users_db[i]
            return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")
