from datetime import datetime
from typing import Optional

from pydantic import (BaseModel, Extra, Field, NonNegativeInt, PositiveInt,
                      validator)

from app.schemas.utils import field_cannot_be_null


class CharityProjectBase(BaseModel):
    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1)
    full_amount: Optional[PositiveInt]

    name_cannot_be_null = validator('name', allow_reuse=True)(
        field_cannot_be_null('Имя проекта не может быть пустым!')
    )
    description_cannot_be_null = validator('description', allow_reuse=True)(
        field_cannot_be_null('Описание проекта не может быть пустым!')
    )
    full_amount_cannot_be_null = validator('full_amount', allow_reuse=True)(
        field_cannot_be_null('Требуемая сумма не может быть пустой!')
    )


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: NonNegativeInt
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
