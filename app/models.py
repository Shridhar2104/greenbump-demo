"""Order models for a small storefront API."""
from datetime import datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, field_validator


class Item(BaseModel):
    model_config = ConfigDict(frozen=True)

    sku: str
    currency: Literal["USD"] = "USD"
    quantity: int = 1
    price_cents: int

    @field_validator("quantity")
    @classmethod
    def quantity_positive(cls, v):
        if v < 1:
            raise ValueError("quantity must be at least 1")
        return v


class Order(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: int
    created_at: datetime
    items: List[Item]
    note: Optional[str] = None

    @field_validator("items")
    @classmethod
    def items_not_empty(cls, v):
        if not v:
            raise ValueError("an order needs at least one item")
        return v

    def total_cents(self) -> int:
        return sum(item.price_cents * item.quantity for item in self.items)
