# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List, Dict

ITEM_NAMES: Dict[str, str] = {
    "AGED_BRIE": "Aged Brie",
    "BACKSTAGE_PASSES": "Backstage passes to a TAFKAL80ETC concert",
    "SULFURAS": "Sulfuras, Hand of Ragnaros",
    "CONJURED": "Conjured Mana Cake",
}


class Item:
    def __init__(self, name: str, sell_in: int, quality: int) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self) -> str:
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose:
    def __init__(self, items: List[Item]) -> None:
        self.items = [ItemFactory.create_item(item) for item in items]

    def update_quality(self) -> None:
        for item in self.items:
            item.update_quality()


class ItemFactory:
    @staticmethod
    def create_item(item: Item) -> "BaseItem":
        if item.name == ITEM_NAMES["AGED_BRIE"]:
            return AgedBrie(item)
        elif item.name == ITEM_NAMES["BACKSTAGE_PASSES"]:
            return BackstagePasses(item)
        elif item.name == ITEM_NAMES["SULFURAS"]:
            return Sulfuras(item)
        elif item.name == ITEM_NAMES["CONJURED"]:
            return ConjuredItem(item)
        else:
            return RegularItem(item)


class BaseItem(ABC):
    def __init__(self, item: Item) -> None:
        self.item = item

    @abstractmethod
    def update_quality(self) -> None:
        pass


class AgedBrie(BaseItem):
    def update_quality(self) -> None:
        if self.item.quality < 50:
            self.item.quality += 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0 and self.item.quality < 50:
            self.item.quality += 1


class BackstagePasses(BaseItem):
    def update_quality(self) -> None:
        if self.item.quality < 50:
            self.item.quality += 1
            if self.item.sell_in < 11 and self.item.quality < 50:
                self.item.quality += 1
            if self.item.sell_in < 6 and self.item.quality < 50:
                self.item.quality += 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0:
            self.item.quality = 0


class Sulfuras(BaseItem):
    def update_quality(self) -> None:
        pass


class RegularItem(BaseItem):
    def update_quality(self) -> None:
        if self.item.quality > 0:
            self.item.quality -= 1
        self.item.sell_in -= 1
        if self.item.sell_in < 0 and self.item.quality > 0:
            self.item.quality -= 1


class ConjuredItem(BaseItem):
    def update_quality(self) -> None:
        if self.item.quality > 0:
            self.item.quality -= 2
        self.item.sell_in -= 1
        if self.item.sell_in < 0 and self.item.quality > 0:
            self.item.quality -= 2
