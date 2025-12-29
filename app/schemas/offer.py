from uuid import UUID
from typing import Optional, List
from pydantic import BaseModel, HttpUrl, Field, ConfigDict


class OfferSchema(BaseModel):
    uuid: UUID
    id: Optional[int] = None
    url: Optional[HttpUrl] = None
    is_active: bool
    name: str
    sum_to: Optional[str] = None
    term_to: Optional[int] = None
    percent_rate: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)


class OfferWallOfferSchema(BaseModel):
    offer: OfferSchema

    model_config = ConfigDict(from_attributes=True)


class OfferWallPopupOfferSchema(BaseModel):
    offer: OfferSchema

    model_config = ConfigDict(from_attributes=True)


class OfferWallSchema(BaseModel):
    token: UUID
    name: Optional[str] = None
    url: Optional[HttpUrl] = None
    description: Optional[str] = None

    offer_assignments: List[OfferWallOfferSchema] = Field(default_factory=list)
    popup_assignments: List[OfferWallPopupOfferSchema] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)


class OfferNamesSchema(BaseModel):
    offer_names: List[str]
