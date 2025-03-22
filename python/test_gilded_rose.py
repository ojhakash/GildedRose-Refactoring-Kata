# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, ITEM_NAMES


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_aged_brie(self):
        # Test normal quality increase
        items = [Item(ITEM_NAMES["AGED_BRIE"], 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

        # Test double increase after sell_in date
        items = [Item(ITEM_NAMES["AGED_BRIE"], 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

        # Test quality cap at 50
        items = [Item(ITEM_NAMES["AGED_BRIE"], 2, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(0, items[0].sell_in)


if __name__ == "__main__":
    unittest.main()
