import decimal

import attrs

from .. import type_defs as _t
from ..config import Config
from ..enum_defs import Coin, EquipmentCategory, ItemWeightFormat


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


@attrs.define
class EquipmentBase:
    category: EquipmentCategory = attrs.field()
    name: str = attrs.field()
    cost: Cost = attrs.field()

    def to_dict(self) -> _t.EquipmentDict:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data: _t.EquipmentDict) -> "EquipmentBase":
        return cls(**data)


@attrs.define
class Armor(EquipmentBase):
    armor_class: int = attrs.field()
    max_dex_bonus: int | None = attrs.field(
        default=None, metadata={"description": "The maximum Dexterity modifier that can be applied to the wearer's AC."}
    )
    strength_requirement: int | None = attrs.field(
        default=None,
        metadata={
            "description": "If not None, the armor reduces the wearer's speed by 10 feet unless the wearer has a Strength score equal to or higher than the requirement."
        },
    )
    stealth_disadvantage: bool = attrs.field(
        default=False, metadata={"description": "If True, the wearer has disadvantage on Stealth checks."}
    )

    def to_dict(self) -> _t.ArmorDict:
        return _t.ArmorDict(**attrs.asdict(self))


@attrs.define
class Item:
    name: str = attrs.field()
    pounds: float = attrs.field(default=0.0, converter=lambda x: round(x, 1))
    slots: int = attrs.field(default=0)
    value: float = attrs.field(default=0.0, converter=lambda x: round(x, 2))
    description: str = attrs.field(default="")

    def to_dict(self) -> _t.ItemDict:
        return _t.ItemDict(**attrs.asdict(self))

    @classmethod
    def from_dict(cls, data: _t.ItemDict) -> "Item":
        return cls(**data)

    @property
    def weight(self) -> float | int:
        weight_format = Config().equipment.WeightFormat
        if weight_format == ItemWeightFormat.POUNDS:
            return self.pounds
        elif weight_format == ItemWeightFormat.SLOTS:
            return self.slots
        else:
            raise ValueError(f"Invalid weight format: {weight_format}")

    @weight.setter
    def weight(self, value: float | int) -> None:
        weight_format = Config().equipment.WeightFormat
        if weight_format == ItemWeightFormat.POUNDS:
            self.pounds = value
        elif weight_format == ItemWeightFormat.SLOTS:
            self.slots = int(value)
        else:
            raise ValueError(f"Invalid weight format: {weight_format}")
