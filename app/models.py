"""Order models for a small storefront API."""
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, validator


class Item(BaseModel):
    sku: str
    currency: str = Field("USD", const=True)
    quantity: int = 1
    price_cents: int

    @validator("quantity")
    def quantity_positive(cls, v):
        if v < 1:
            raise ValueError("quantity must be at least 1")
        return v

    class Config:
        allow_mutation = False


class Order(BaseModel):
    id: int
    created_at: datetime
    items: List[Item]
    note: Optional[str] = None

    @validator("items")
    def items_not_empty(cls, v):
        if not v:
            raise ValueError("an order needs at least one item")
        return v

    def total_cents(self) -> int:
        return sum(item.price_cents * item.quantity for item in self.items)

    class Config:
        allow_mutation = False
