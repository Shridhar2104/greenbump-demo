from datetime import datetime

import pytest
from pydantic import ValidationError

from app.models import Item, Order
from app.serializers import (
    order_from_dict,
    order_from_json,
    order_schema,
    order_to_dict,
    order_to_json,
)


def make_order() -> Order:
    return Order(
        id=7,
        created_at=datetime(2026, 1, 5, 12, 0, 0),
        items=[
            Item(sku="TEA-001", quantity=2, price_cents=450),
            Item(sku="MUG-140", price_cents=1200),
        ],
        note="gift wrap",
    )


def test_total_cents_sums_quantity_times_price():
    assert make_order().total_cents() == 2 * 450 + 1200


def test_dict_roundtrip():
    order = make_order()
    assert order_from_dict(order_to_dict(order)) == order


def test_json_roundtrip():
    order = make_order()
    assert order_from_json(order_to_json(order)) == order


def test_schema_lists_fields():
    props = order_schema()["properties"]
    assert set(props) >= {"id", "created_at", "items", "note"}


def test_quantity_must_be_positive():
    with pytest.raises(ValidationError):
        Item(sku="TEA-001", quantity=0, price_cents=450)


def test_order_needs_items():
    with pytest.raises(ValidationError):
        Order(id=1, created_at=datetime(2026, 1, 5), items=[])


def test_currency_is_fixed():
    with pytest.raises(ValidationError):
        Item(sku="TEA-001", currency="EUR", price_cents=450)


def test_items_are_immutable():
    item = Item(sku="TEA-001", price_cents=450)
    with pytest.raises(Exception):
        item.quantity = 5


def test_note_is_optional():
    order = Order(id=2, created_at=datetime(2026, 1, 5), items=[Item(sku="X", price_cents=1)])
    assert order.note is None


def test_from_dict_validates():
    with pytest.raises(ValidationError):
        order_from_dict({"id": "not-even-close"})
