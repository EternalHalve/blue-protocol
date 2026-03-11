from pydantic import BaseModel, EmailStr, Field, AfterValidator, ConfigDict
from datetime import datetime
from typing import Optional, Annotated
import string


def validate_password_strength(password: str) -> str:
    checks = [
        (any(c.isdigit() for c in password), "digit"),
        (any(c.isupper() for c in password), "uppercase letter"),
        (any(c.islower() for c in password), "lowercase letter"),
        (any(c in string.punctuation for c in password), "special character"),
    ]
    for passed, entity in checks:
        if not passed:
            raise ValueError(
                f"Security Breach: Password requires at least one {entity}."
            )
    return password


UsernameField = Annotated[
    str,
    Field(
        min_length=3,
        max_length=50,
        pattern="^[a-zA-Z0-9_.-]+$",
        examples=["maggots"],
    ),
]
StrongPassword = Annotated[
    str,
    Field(min_length=8, max_length=128, examples=["Ryo_Eat_Grass!23"]),
    AfterValidator(validate_password_strength),
]


class UserBase(BaseModel):
    username: UsernameField
    email: EmailStr


class UserCreate(UserBase):
    password: StrongPassword


class UserUpdate(BaseModel):
    username: Optional[UsernameField] = None
    email: Optional[EmailStr] = None
    password: Optional[StrongPassword] = None


class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class DeleteAccountConfirmation(BaseModel):
    password: str
    confirm_text: str
