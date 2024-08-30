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


def _decimal_serializer(inst: attrs.AttrsInstance, field: t.Any, value: t.Any) -> t.Any:
    return str(value) if isinstance(value, decimal.Decimal) else value


@attrs.define
class Item:
    name: str = attrs.field()
    pounds: decimal.Decimal = attrs.field(default=D(0.0))
    slots: int = attrs.field(default=0)
    cost: decimal.Decimal = attrs.field(default=D(0.00))
    description: str = attrs.field(default="")

    def to_dict(self) -> _t.ItemDict:
        # Turn decimal.Decimal instances into strings for JSON serialization
        return _t.ItemDict(**attrs.asdict(self, value_serializer=_decimal_serializer))

    @classmethod
    def from_dict(cls, data: _t.ItemDict) -> "Item":
        # Ensure that cost and pounds are Decimal instances
        data["cost"] = D(data["cost"])
        data["pounds"] = D(data["pounds"])
        return cls(**data)

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
