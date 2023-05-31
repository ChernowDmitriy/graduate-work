from fastapi import APIRouter

from .v1 import router as _router

router = APIRouter(
    prefix='/api/v1'
)

router.include_router(_router)
