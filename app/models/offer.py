import uuid
from enum import Enum
from typing import Optional

from sqlalchemy import (
    Integer,
    String,
    Boolean,
    Text,
    ForeignKey,
    UniqueConstraint,
    Enum as SAEnum,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class OfferChoices(str, Enum):
    Loanplus = "Loanplus"
    SgroshiCPA2 = "SgroshiCPA2"
    Novikredyty = "Novikredyty"
    TurboGroshi = "TurboGroshi"
    Crypsee = "Crypsee"
    Suncredit = "Suncredit"
    Lehko = "Lehko"
    Monto = "Monto"
    Limon = "Limon"
    Amigo = "Amigo"
    FirstCredit = "FirstCredit"
    Finsfera = "Finsfera"
    Pango = "Pango"
    Treba = "Treba"
    StarFin = "StarFin"
    BitCapital = "BitCapital"
    SgroshiCPL = "SgroshiCPL"
    LoviLave = "LoviLave"
    Prostocredit = "Prostocredit"
    Sloncredit = "Sloncredit"
    Clickcredit = "Clickcredit"
    Credos = "Credos"
    Dodam = "Dodam"
    SelfieCredit = "SelfieCredit"
    Egroshi = "Egroshi"
    Alexcredit = "Alexcredit"
    SgroshiCPA1 = "SgroshiCPA1"
    Tengo = "Tengo"
    Credit7 = "Credit7"
    Tpozyka = "Tpozyka"
    Creditkasa = "Creditkasa"
    Moneyveo = "Moneyveo"
    My_Credit = "MyCredit"
    Credit_Plus = "CreditPlus"
    Miloan = "Miloan"
    Avans = "AvansCredit"


class Offer(Base):
    __tablename__ = "offer"

    uuid: Mapped[str] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    id: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    name: Mapped[OfferChoices] = mapped_column(
        SAEnum(OfferChoices), unique=True, nullable=False
    )
    sum_to: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    term_to: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    percent_rate: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    wall_assignments: Mapped[list["OfferWallOffer"]] = relationship(
        back_populates="offer", cascade="all, delete-orphan"
    )
    popup_assignments: Mapped[list["OfferWallPopupOffer"]] = relationship(
        back_populates="offer", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Offer name={self.name!r} active={self.is_active}>"


class OfferWall(Base):
    __tablename__ = "offer_wall"

    token: Mapped[str] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    url: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    offer_assignments: Mapped[list["OfferWallOffer"]] = relationship(
        back_populates="offer_wall",
        cascade="all, delete-orphan",
        order_by="OfferWallOffer.order",
    )
    popup_assignments: Mapped[list["OfferWallPopupOffer"]] = relationship(
        back_populates="offer_wall",
        cascade="all, delete-orphan",
        order_by="OfferWallPopupOffer.order",
    )

    def __repr__(self):
        return f"<OfferWall token={self.token}>"


class OfferWallOffer(Base):
    __tablename__ = "offer_wall_offer"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    offer_wall_token: Mapped[str] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("offer_wall.token", ondelete="CASCADE")
    )
    offer_uuid: Mapped[str] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("offer.uuid", ondelete="CASCADE")
    )
    order: Mapped[int] = mapped_column(Integer, default=0)

    offer_wall: Mapped["OfferWall"] = relationship(back_populates="offer_assignments")
    offer: Mapped["Offer"] = relationship(back_populates="wall_assignments")

    __table_args__ = (UniqueConstraint("offer_wall_token", "offer_uuid"),)

    def __repr__(self):
        return f"<OfferWallOffer offer={self.offer_uuid} wall={self.offer_wall_token}>"


class OfferWallPopupOffer(Base):
    __tablename__ = "offer_wall_popup_offer"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    offer_wall_token: Mapped[str] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("offer_wall.token", ondelete="CASCADE")
    )
    offer_uuid: Mapped[str] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("offer.uuid", ondelete="CASCADE")
    )
    order: Mapped[int] = mapped_column(Integer, default=0)

    offer_wall: Mapped["OfferWall"] = relationship(back_populates="popup_assignments")
    offer: Mapped["Offer"] = relationship(back_populates="popup_assignments")

    __table_args__ = (UniqueConstraint("offer_wall_token", "offer_uuid"),)

    def __repr__(self):
        return f"<OfferWallPopupOffer offer={self.offer_uuid} wall={self.offer_wall_token}>"
