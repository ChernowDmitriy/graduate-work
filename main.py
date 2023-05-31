from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import router as api_router
from infrastructures.database import BaseModel, engine

app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
