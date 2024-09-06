import decimal
import typing as t

import attrs

from .. import type_defs as _t
from ..config import Config
from ..enum_defs import Coin, ItemWeightFormat

D = decimal.Decimal


@attrs.define
class Cost:
    unit: Coin = attrs.field()
    quantity: int = attrs.field(default=0)

    def __str__(self) -> str:
        return f"{self.quantity} {str(self.unit).upper()}"

    def to_dict(self) -> _t.CostDict:
        return {
            "unit": self.unit.value.name,
            "quantity": self.quantity,
        }

    @classmethod
    def from_dict(cls, data: _t.CostDict) -> "Cost":
        unit = Coin[data["unit"].upper()]
        return cls(unit=unit, quantity=data["quantity"])

    @property
    def copper(self) -> decimal.Decimal:
        return self.unit.copper_exchange_rate * self.quantity

    @property
    def silver(self) -> decimal.Decimal:
        return self.unit.silver_exchange_rate * self.quantity

    @property
    def electrum(self) -> decimal.Decimal:
        return self.unit.electrum_exchange_rate * self.quantity

    @property
    def gold(self) -> decimal.Decimal:
        return self.unit.gold_exchange_rate * self.quantity

    @property
    def platinum(self) -> decimal.Decimal:
        return self.unit.platinum_exchange_rate * self.quantity


def _item_serializer(inst: attrs.AttrsInstance, field: t.Any, value: t.Any) -> t.Any:
    if isinstance(value, decimal.Decimal):
        return str(value)
    elif isinstance(value, Cost):
        return value.to_dict()
    else:
        return value


@attrs.define
class Item:
    name: str = attrs.field()
    category: str = attrs.field(default="")
    pounds: decimal.Decimal = attrs.field(default=D(0.0))
    slots: int = attrs.field(default=0)
    cost: Cost = attrs.field(default=Cost(unit=Coin.GOLD, quantity=0))
    description: str = attrs.field(default="")

    def to_dict(self) -> _t.ItemDict:
        return _t.ItemDict(**attrs.asdict(self, value_serializer=_item_serializer))

    @classmethod
    def from_dict(cls, data: _t.ItemDict) -> "Item":
        cost = Cost.from_dict(data["cost"])
        return cls(
            name=data["name"],
            category=data["category"],
            pounds=D(data["pounds"]),
            slots=int(data["slots"]),
            cost=cost,
            description=data["description"],
        )

    @property
    def weight(self) -> decimal.Decimal | int:
        weight_format = Config().equipment.WeightFormat
        if weight_format == ItemWeightFormat.POUNDS:
            return self.pounds
        elif weight_format == ItemWeightFormat.SLOTS:
            return self.slots
        else:
            raise ValueError(f"Invalid weight format: {weight_format}")

    @weight.setter
    def weight(self, value: decimal.Decimal | int) -> None:
        weight_format = Config().equipment.WeightFormat
        if weight_format == ItemWeightFormat.POUNDS:
            self.pounds = D(value)
        elif weight_format == ItemWeightFormat.SLOTS:
            self.slots = int(value)
        else:
            raise ValueError(f"Invalid weight format: {weight_format}")
