from pydantic import BaseModel, EmailStr, Field, AfterValidator, ConfigDict
from datetime import datetime
from typing import Optional, Annotated
import string

def validate_password_strength(password: str) -> str:
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit.")
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not any(char in string.punctuation for char in password):
        raise ValueError("Password must contain at least one special character.")
    return password


ValidatedPassword = Annotated[
    str, Field(min_length=8, max_length=128), AfterValidator(validate_password_strength)
]
UsernameField = Annotated[
    str, Field(min_length=3, max_length=50, pattern="^[a-zA-Z0-9_.-]+$", examples=["johndoe_99"])
]
PasswordField = Annotated[str, Field(min_length=8, max_length=128)]

class UserBase(BaseModel):
    username: UsernameField
    email: EmailStr


class UserCreate(UserBase):
    password: ValidatedPassword


class UserUpdate(BaseModel):
    username: Optional[UsernameField] = None
    email: Optional[EmailStr] = None
    password: Optional[ValidatedPassword] = None
    is_active: Optional[bool] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"