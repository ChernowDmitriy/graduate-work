from fastapi import HTTPException as FastAPIHTTPException
from starlette import status
from starlette.exceptions import HTTPException

InvalidCredentials = FastAPIHTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid email or password"
)

UserEmailAlreadyExistsException = FastAPIHTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail='User with this email already exists'
)

SignatureVerificationFailed = FastAPIHTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid token",
    headers={"WWW-Authenticate": "Bearer"}
)

TokenNotProvided = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='The token must be provided'
)
