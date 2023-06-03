from fastapi import Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, JWTError, ExpiredSignatureError
from passlib.exc import InvalidTokenError

from core.domains import User
from core.exceptions import SignatureVerificationFailed
from core.services.user_service import UserService
from infrastructures.config.base import get_settings
from infrastructures.dependencies import get_user_service

settings = get_settings()


security_scheme = HTTPBearer()


def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, settings.HASHING_ALGORITHM)
        return payload
    except (InvalidTokenError, ExpiredSignatureError, JWTError):
        raise SignatureVerificationFailed


def encode_token(payload: dict) -> str:
    encoded_jwt = jwt.encode(payload,
                             settings.JWT_SECRET,
                             algorithm=settings.HASHING_ALGORITHM)
    return encoded_jwt


async def get_current_user(
        auth_credentials: HTTPAuthorizationCredentials = Depends(security_scheme),
        user_service: UserService = Depends(get_user_service)
) -> User:
    payload = verify_token(auth_credentials.credentials)
    user_id = payload.get("sub")
    user = await user_service.get_user_by_id(user_id)
    return user


async def has_access(credentials: HTTPAuthorizationCredentials = Depends(security_scheme)):
    verify_token(credentials.credentials)
