# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose, ITEM_NAMES


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item(self):
        # Test normal quality decrease
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

        # Test quality decrease after sell_in date
        items = [Item("+5 Dexterity Vest", 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

        # Test quality never goes below 0
        items = [Item("+5 Dexterity Vest", 3, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(2, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(1, items[0].sell_in)

        # Test with negative sell_in
        items = [Item("+5 Dexterity Vest", -1, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(18, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

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

    def test_backstage_passes(self):
        # Test normal quality increase
        items = [Item(ITEM_NAMES["BACKSTAGE_PASSES"], 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(21, items[0].quality)
        self.assertEqual(14, items[0].sell_in)

        # Test quality increases by 2 when 10 days or less
        items = [Item(ITEM_NAMES["BACKSTAGE_PASSES"], 10, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(22, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

        # Test quality increases by 3 when 5 days or less
        items = [Item(ITEM_NAMES["BACKSTAGE_PASSES"], 5, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(23, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

        # Test quality cap at 50
        items = [Item(ITEM_NAMES["BACKSTAGE_PASSES"], 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(4, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(3, items[0].sell_in)

        # Test quality stays at 0 after concert
        items = [Item(ITEM_NAMES["BACKSTAGE_PASSES"], 0, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    def test_sulfuras(self):
        # Test quality and sell_in never change
        items = [Item(ITEM_NAMES["SULFURAS"], 0, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

        # Test with negative sell_in
        items = [Item(ITEM_NAMES["SULFURAS"], -1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

        # Test with different quality value
        items = [Item(ITEM_NAMES["SULFURAS"], 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(0, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(0, items[0].sell_in)

    def test_conjured(self):
        # Test normal quality decrease (twice as fast)
        items = [Item(ITEM_NAMES["CONJURED"], 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(2, items[0].sell_in)

        # Test quality decrease after sell_in date (twice as fast)
        items = [Item(ITEM_NAMES["CONJURED"], 0, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

        # Test quality never goes below 0
        items = [Item(ITEM_NAMES["CONJURED"], 2, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(1, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(0, items[0].sell_in)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

        # Test with negative sell_in
        items = [Item(ITEM_NAMES["CONJURED"], -1, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)
        self.assertEqual(-2, items[0].sell_in)

    

if __name__ == "__main__":
    unittest.main()
