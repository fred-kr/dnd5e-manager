import decimal
import typing as t

import attrs

from .. import type_defs as _t
from ..config import Config
from ..enum_defs import CurrencyType, ItemWeightFormat

D = decimal.Decimal


class CostValues(t.NamedTuple):
    copper: decimal.Decimal
    silver: decimal.Decimal
    electrum: decimal.Decimal
    gold: decimal.Decimal
    platinum: decimal.Decimal

    def __str__(self) -> str:
        return "\n".join(f"{v} {str(k).title()}" for k, v in self._asdict().items())


@attrs.define(order=True)
class Cost:
    display_currency: CurrencyType = attrs.field(default=CurrencyType.GOLD, order=False)
    # Quantity is the amount in copper coins since it's the smallest unit. Methods for converting to and from other coins are provided.
    quantity: int = attrs.field(default=0)

    @classmethod
    def from_currency(cls, currency: CurrencyType, amount: _t.Number) -> "Cost":
        d_amount = round(D(amount), 3)
        if currency == CurrencyType.COPPER:
            quantity = int(d_amount)
        elif currency == CurrencyType.SILVER:
            quantity = int(d_amount * 10)
        elif currency == CurrencyType.ELECTRUM:
            quantity = int(d_amount * 50)
        elif currency == CurrencyType.GOLD:
            quantity = int(d_amount * 100)
        elif currency == CurrencyType.PLATINUM:
            quantity = int(d_amount * 1000)
        else:
            raise ValueError(f"Invalid currency type: {currency}")
        return cls(currency, quantity)

    def __str__(self) -> str:
        return f"{self.quantity} {self.display_currency}"

    def to_dict(self) -> _t.CostDict:
        return {
            "display_currency": self.display_currency.symbol,
            "quantity": str(self.to_currency(self.display_currency)),
        }

    @classmethod
    def from_dict(cls, data: _t.CostDict) -> "Cost":
        curr_type = CurrencyType(data["display_currency"])
        return cls.from_currency(curr_type, data["quantity"])

    def to_currency(self, unit: CurrencyType) -> decimal.Decimal:
        if unit == CurrencyType.COPPER:
            return D(self.quantity)
        elif unit == CurrencyType.SILVER:
            return D(self.quantity) / D(10)
        elif unit == CurrencyType.ELECTRUM:
            return D(self.quantity) / D(50)
        elif unit == CurrencyType.GOLD:
            return D(self.quantity) / D(100)
        elif unit == CurrencyType.PLATINUM:
            return D(self.quantity) / D(1000)
        else:
            raise ValueError(f"Invalid currency type: {unit}")

    @property
    def converted_values(self) -> CostValues:
        return CostValues(
            copper=self.to_currency(CurrencyType.COPPER),
            silver=self.to_currency(CurrencyType.SILVER),
            electrum=self.to_currency(CurrencyType.ELECTRUM),
            gold=self.to_currency(CurrencyType.GOLD),
            platinum=self.to_currency(CurrencyType.PLATINUM),
        )


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
    # TODO: Use EquipmentCategoriesIndex for category
    category: str = attrs.field(default="")
    pounds: decimal.Decimal = attrs.field(default=D(0.0))
    slots: int = attrs.field(default=0)
    cost: Cost = attrs.field(factory=Cost)
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
