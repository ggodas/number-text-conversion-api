from fastapi import APIRouter

from .endpoints.encoder_api import encoder_route
from .endpoints.decoder_api import decoder_route

api_router = APIRouter()
api_router.include_router(encoder_route, prefix="/encoder", tags=["encoder"])
api_router.include_router(decoder_route, prefix="/decoder", tags=["decoder"])
