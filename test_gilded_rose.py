# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_brie_should_increase_after_one_day(self):
        brie = "Aged Brie"
        items = [Item(brie, 1, 2)]
        gr = GildedRose(items)

        gr.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_sulfuras_should_remain_same_after_one_day(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 2, 3)]
        gr = GildedRose(items)

        gr.update_quality()
        self.assertEqual(2, items[0].quality)

    def test_quality_never_more_than_50(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 50)]
        gr = GildedRose(items)

        gr.update_quality()
        self.assertEqual(51, items[0].quality)


if __name__ == '__main__':
    unittest.main()
