from jose import jwt, JWTError, ExpiredSignatureError
from passlib.exc import InvalidTokenError

from core.exceptions import SignatureVerificationFailed
from infrastructures.config.base import get_settings

settings = get_settings()


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
