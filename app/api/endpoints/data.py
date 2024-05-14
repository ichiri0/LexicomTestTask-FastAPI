from typing import Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import ValidationError

from app import schemas
from app.core.utils.redis_client import RedisClient

router = APIRouter()

# При существовании данных с таким ключём - его адрес будет перезаписан, 
# Можно создать впринципе на такой же uri контроллер с методом put, но это будет дубликат кода
@router.post("/write_data")
async def write_data(data: schemas.DataSchema):

    redis_client = RedisClient()

    redis_client.rd.set(data.phone, data.address)

    return schemas.DataSchema(
        phone=data.phone,
        address=data.address,
    )


@router.get("/check_data", response_model=Optional[schemas.DataSchema])
async def check_data(phone: str):

    redis_client = RedisClient()

    address = redis_client.rd.get(phone)
    if address is None:

        raise HTTPException(
            status_code=404,
            detail="Not found"
        )

    try:
        return schemas.DataSchema(
            phone=phone,
            address=address.decode("utf-8")
        )
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(e)
        )
