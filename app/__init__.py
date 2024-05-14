from fastapi import FastAPI

from app import api
from app.core import settings

app = FastAPI(title="Lexicom Test Task",
              openapi_url=f"{settings.APP_API_PREFIX}/openapi.json")


def shutdown():
    ...


async def startup():
    ...

app.add_event_handler("shutdown", shutdown)
app.add_event_handler("startup", startup)


app.include_router(api.api_router,
                   prefix=settings.APP_API_PREFIX,
                   )
