"""
Модуль с зависимостями для FastAPI.
"""


from app.database import Database, new_session


async def get_db():
    session = await new_session()
    try:
        yield Database(session)
    finally:
        await session.close()

