from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import OfferWall, OfferWallOffer, OfferWallPopupOffer


class OfferWallRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_token(self, token: UUID) -> Optional[OfferWall]:
        result = await self.session.execute(
            select(OfferWall)
            .options(
                selectinload(OfferWall.offer_assignments).selectinload(
                    OfferWallOffer.offer
                ),
                selectinload(OfferWall.popup_assignments).selectinload(
                    OfferWallPopupOffer.offer
                ),
            )
            .where(OfferWall.token == token)
        )
        return result.scalar_one_or_none()
