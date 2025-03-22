# -*- coding: utf-8 -*-

# Item name constants
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"

class GildedRose(object):

    def __init__(self, items):
        self.items = [ShopItem(item) for item in items]

    def update_quality(self):
        for item in self.items:
            item.update_quality()

class ShopItem:
    def __init__(self, item):
        self.item = item

    def update_quality(self):
        if self.item.name != BACKSTAGE_PASSES and self.item.name != AGED_BRIE:
            if self.item.name != SULFURAS and self.item.quality > 0:
                self.item.quality = self.item.quality - 1
        else:
            if self.item.quality < 50:
                self.item.quality = self.item.quality + 1
                if self.item.name == BACKSTAGE_PASSES:
                    if self.item.sell_in < 11 and self.item.quality < 50:
                            self.item.quality = self.item.quality + 1
                    if self.item.sell_in < 6 and self.item.quality < 50:
                            self.item.quality = self.item.quality + 1
        if self.item.name != SULFURAS:
            self.item.sell_in = self.item.sell_in - 1
        if self.item.sell_in < 0:
            if self.item.name != AGED_BRIE:
                if self.item.name != BACKSTAGE_PASSES:
                    if self.item.name != SULFURAS and self.item.quality > 0:
                            self.item.quality = self.item.quality - 1
                else:
                    self.item.quality = 0
            else:
                if self.item.quality < 50:
                    self.item.quality = self.item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
