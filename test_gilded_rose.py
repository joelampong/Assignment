# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     print(items[0])
    #     gilded_rose.update_quality()
    #     print(items[0])
    #     self.assertEquals(True,True)

      def test_backstage(self):
         items = [ Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),]
         gilded_rose = GildedRose(items)
         print(items[0])
         gilded_rose.update_quality()
         print(items[0])
         self.assertEquals(True,True) 
      def test_conjured(self):
         items = [ Item(name="Conjured Mana Cake", sell_in=3, quality=6),]
         gilded_rose = GildedRose(items)
         item = [ Item(name="Conjured Mana Cake", sell_in=2, quality=5),]

         gilded_rose.update_quality()
         self.assertEqual(items[0],item[0])
     
    
if __name__ == '__main__':
    unittest.main()
