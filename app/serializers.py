"""Serialization helpers used by the API layer."""
from .models import Order


def order_to_dict(order: Order) -> dict:
    return order.dict()


def order_to_json(order: Order) -> str:
    return order.json()


def order_from_dict(data: dict) -> Order:
    return Order.parse_obj(data)


def order_from_json(raw: str) -> Order:
    return Order.parse_raw(raw)


def order_schema() -> dict:
    return Order.schema()
