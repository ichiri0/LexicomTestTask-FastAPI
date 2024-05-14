import redis

from app.core import settings


class RedisClient():
    '''
    Класс инициалицазии Redis
    '''
    def __init__(self) -> None:
        self.rd = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB
        )
