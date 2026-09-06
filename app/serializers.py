"""Serialization helpers used by the API layer."""
from .models import Order


def order_to_dict(order: Order) -> dict:
    return order.model_dump()


def order_to_json(order: Order) -> str:
    return order.model_dump_json()


def order_from_dict(data: dict) -> Order:
    return Order.model_validate(data)


def order_from_json(raw: str) -> Order:
    return Order.model_validate_json(raw)


def order_schema() -> dict:
    return Order.model_json_schema()
