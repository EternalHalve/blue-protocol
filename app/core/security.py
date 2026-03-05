from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt

from core.config import CONFIG

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def verify_pass(plain_pass: str, hashed_pass: str) -> bool:
    return pwd_context.verify(plain_pass, hashed_pass)

def get_pass_hash(password: str) -> str:
    return pwd_context.hash(password)

def _create_token(
    data: dict, expires_delta: timedelta | None, token_type: str, default_minutes: int
) -> str:
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=default_minutes)
    )
    to_encode.update({"exp": expire, "type": token_type})
    return jwt.encode(to_encode, CONFIG.SECRET_KEY, algorithm=CONFIG.ALGORITHM)

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    return _create_token(
        data, expires_delta, "access", CONFIG.ACCESS_TOKEN_EXPIRE_MINUTES
    )