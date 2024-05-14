"""
API Проекта
"""

from fastapi import APIRouter, status, HTTPException

from .endpoints import data

api_router = APIRouter()

@api_router.get("")
async def api_check():
    return HTTPException(status_code=status.HTTP_200_OK, detail="ok")


api_router.include_router(data.router, prefix="/words", tags=["words"])
