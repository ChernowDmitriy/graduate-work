from fastapi import HTTPException
from starlette import status

InvalidCredentials = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid email or password"
)

UserEmailAlreadyExistsException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='User with this email already exists'
)

SignatureVerificationFailed = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token",
    headers={"WWW-Authenticate": "Bearer"}
)
