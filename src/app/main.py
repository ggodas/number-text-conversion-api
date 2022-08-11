from app.settings import TITLE, VERSION, CONTACT, DESCRIPTION, TAGS_METADATA, API_V1_STR
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from .api.router import api_router

app = FastAPI(
    title=TITLE,
    version=VERSION,
    contact=CONTACT,
    description=DESCRIPTION,
    openapi_tags=TAGS_METADATA,
    openapi_url=f"{API_V1_STR}/openapi.json",
)
app.include_router(api_router, prefix=API_V1_STR)


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=418,
        content={"message": "Oops! did something wrong."},
    )
