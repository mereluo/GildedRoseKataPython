# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_aged_brie_increases_in_quality(self):
        items = [Item("Aged Brie", 2, 0)]
        gr = GildedRose(items)
        gr.update_items(items[0])
        self.assertEqual(items[0].quality, 1)  # Quality increases by 1
        self.assertEqual(items[0].sell_in, 1)  # SellIn decreases by 1

    def test_sulfuras_quality_constant(self):
        items = [Item("Sulfuras", 0, 80)]
        gr = GildedRose(items)
        gr.update_items(items[0])
        self.assertEqual(items[0].quality, 80)
        self.assertEqual(items[0].sell_in, 0)

    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gr = GildedRose(items)
        gr.update_items(items[0])
        self.assertEqual(items[0].quality, 4)  # Quality decreases by 2
        self.assertEqual(items[0].sell_in, 2)  # SellIn decreases by 1

    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gr = GildedRose(items)
        gr.update_items(items[0])
        self.assertEqual(items[0].quality, 21)  # Quality increases by 1
        self.assertEqual(items[0].sell_in, 14)

        # Update within 10 days of concert (quality increases by 2)
        items[0].sell_in = 10
        gr.update_items(items[0])
        self.assertEqual(items[0].quality, 23)  # Quality increases by 2


if __name__ == '__main__':
    unittest.main()
