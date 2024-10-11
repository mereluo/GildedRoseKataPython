# -*- coding: utf-8 -*-

class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):
    maxQuality = 50
    minQuality = 0
    sulfurasQuality = 80
    sulfurasSellin = 0

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_items(self, item):
        name = item.name.lower()
        if name == "aged brie":
            self.update_brie(item)
        elif name == "sulfuras":
            self.update_sulfuras(item)
        elif "backstage" in name:
            self.update_backstage(item)
        elif "conjured" in name:
            self.update_conjured(item)
        else:
            self.update_basic(item)

    def update_brie(self, item):
        item.sell_in -= 1
        if item.quality < self.maxQuality:
            item.quality += 1
            # post sell_in days, rate doubled
            if item.sell_in < 0 and item.quality < self.maxQuality:
                item.quality += 1

    def update_sulfuras(self, item):
        item.quality = self.sulfurasQuality
        item.sell_in = self.sulfurasSellin

    def update_backstage(self, item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            if item.quality + 3 <= self.maxQuality:
                item.quality += 3
            else:
                item.quality = self.maxQuality
        elif item.sell_in < 10:
            if item.quality + 2 <= self.maxQuality:
                item.quality += 2
            else:
                item.quality = self.maxQuality
        else:
            if item.quality < self.maxQuality:
                item.quality += 1

    def update_conjured(self, item):
        item.sell_in -= 1
        # degrade twice as fast
        degradation = 2
        if item.sell_in < 0:
            degradation *= 2
        item.quality -= degradation
        if item.quality < self.minQuality:
            item.quality = self.minQuality

    def update_basic(self, item):
        item.sell_in -= 1
        degradation = 1
        if item.sell_in < 0:
            degradation *= 2
        item.quality -= degradation
        if item.quality < self.minQuality:
            item.quality = self.minQuality

# class GildedRose(object):

#     def __init__(self, items: list[Item]):
#         # DO NOT CHANGE THIS ATTRIBUTE!!!
#         self.items = items

#     def update_quality(self):
#         for item in self.items:
#             if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
#                 if item.quality > 0:
#                     if item.name != "Sulfuras, Hand of Ragnaros":
#                         item.quality = item.quality - 1
#             else:
#                 if item.quality < 50:
#                     item.quality = item.quality + 1
#                     if item.name == "Backstage passes to a TAFKAL80ETC concert":
#                         if item.sell_in < 11:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#                         if item.sell_in < 6:
#                             if item.quality < 50:
#                                 item.quality = item.quality + 1
#             if item.name != "Sulfuras, Hand of Ragnaros":
#                 item.sell_in = item.sell_in - 1
#             if item.sell_in < 0:
#                 if item.name != "Aged Brie":
#                     if item.name != "Backstage passes to a TAFKAL80ETC concert":
#                         if item.quality > 0:
#                             if item.name != "Sulfuras, Hand of Ragnaros":
#                                 item.quality = item.quality - 1
#                     else:
#                         item.quality = item.quality - item.quality
#                 else:
#                     if item.quality < 50:
#                         item.quality = item.quality + 1
