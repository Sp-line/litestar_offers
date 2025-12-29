from litestar import Litestar
from litestar.openapi import OpenAPIConfig

from app.db import init_db
from app.services.offer import OfferWallController
from app.config import settings
from litestar.config.cors import CORSConfig


async def on_startup() -> None:
    await init_db()


def build_app() -> Litestar:
    route_handlers = [OfferWallController]

    cors_config = CORSConfig(
        allow_origins=list(settings.CORS_ORIGINS),
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    openapi = OpenAPIConfig(title="Litestar Offers API", version="1.0.0")

    return Litestar(
        route_handlers=route_handlers,
        debug=settings.DEBUG,
        openapi_config=openapi,
        cors_config=cors_config,
        on_startup=[on_startup],
    )


app = build_app()
