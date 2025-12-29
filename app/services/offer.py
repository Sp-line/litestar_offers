from uuid import UUID

from litestar import Controller, get
from litestar.di import Provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.exceptions import NotFound
from app.models.offer import (
    OfferChoices,
)
from app.repositories.offer import OfferWallRepository
from app.schemas.offer import OfferWallSchema, OfferNamesSchema


class OfferWallController(Controller):
    path = "/offerwalls"
    dependencies = {"session": Provide(get_session)}

    @get("/offer-names")
    async def get_offer_names(self) -> OfferNamesSchema:
        return OfferNamesSchema(offer_names=[choice.value for choice in OfferChoices])

    @get("/{token:str}", summary="Get OfferWall by token")
    async def get_offer_wall(
        self, token: UUID, session: AsyncSession
    ) -> OfferWallSchema:
        repo = OfferWallRepository(session)
        offer_wall = await repo.get_by_token(token)
        if not offer_wall:
            return NotFound.to_response()

        return OfferWallSchema.model_validate(offer_wall)
