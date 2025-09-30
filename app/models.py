from pydantic import BaseModel, EmailStr, Field, validator
from datetime import datetime
import re, uuid

class User(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    username: str = Field(..., min_length=6, max_length=15, pattern="^[a-z0-9]+$")
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20)
    role: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @validator("role")
    def validate_role(cls, v):
        if v not in ["admin", "staff"]:
            raise ValueError("role must be admin or staff")
        return v

    @validator("password")
    def validate_password(cls, v):
        if not re.search(r"[A-Z]", v): raise ValueError("need uppercase")
        if not re.search(r"[a-z]", v): raise ValueError("need lowercase")
        if not re.search(r"\d", v): raise ValueError("need digit")
        if not re.search(r"[!@]", v): raise ValueError("need ! or @")
        return v
