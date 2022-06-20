# -*- coding: utf-8 -*-

class GildedRose(object):
    #control parameters
    UPPER_QUALITY_ALLOWED = 50;
    LOWER_QUALITY_ALLOWED = 0;
    SELLI_TO_INCREMENT_BY_THREE = 5;
    SELLI_TO_INCREMENT_BY_TWO = 10;
    def __init__(self, items):
        self.items = items
    #function to check if item is Aged Brie    
    def isBrie(self,item):
        return "Aged Brie" == item.name 
    #function to check if item is BackStage
    def isBackstage(self,item):
        return "Backstage passes" in item.name  
    #function to check if item is Sulfuras     
    def isSulfuras(self,item):
        return "Sulfuras" in item.name
    #function to check if item is Conured     
    def isConjured(self,item):
        return "Conjured" in item.name
    #degrade Quality
    def degradeQuality(self,item):
        if (self.isConjured(item)): #check if it is conjured item the quality will degrade twice as normal item
            return  item.quality - 2  
        return item.quality - 1  
    #increase Quality depending upon special items
    def increaseQuality(self,item):
        inc=1
        if (item.sell_in <= self.SELLI_TO_INCREMENT_BY_TWO):
            inc = 2
        if (item.sell_in <= self.SELLI_TO_INCREMENT_BY_THREE):
            inc = 3
     
        return item.quality + inc; 
     #decrease sellin value of item
    def decrease_sellin(self,item):
        return item.sell_in - 1  
    #check for validity of quality
    def isQualityValid(self,item):
        return (item.quality > self.LOWER_QUALITY_ALLOWED) and (item.quality < self.UPPER_QUALITY_ALLOWED )    
    #checkfor whether to increase quality or not that depends on special items  
    def isIncreasingQualityItem(self,item):
        return self.isBrie(item) or self.isBackstage(item) 
    #checkfor whether to decrease in quality or not that depends on other items 
    def isDecreasingQualityItem(self,item):
        return (not self.isIncreasingQualityItem(item) and not self.isSulfuras(item)and self.isQualityValid(item))
    #checkfor whether to decrease in sellin  or not that depends on other items     
    def isDecreasingsell_inItem(self,item):
        return  not self.isSulfuras(item)
    #update values of sell in
    def updateItemsell_in(self,item):
        sell_in = item.sell_in
        if (self.isDecreasingsell_inItem(item)):
            sell_in = self.decrease_sellin(item)
        return sell_in


#performed changes i n update quality
    def update_quality(self):

        #iterating over each item
        for item in self.items:
               if (self.isDecreasingQualityItem(item)):
                item.quality = self.degradeQuality(item)

               if (self.isIncreasingQualityItem(item)):
                item.quality = self.increaseQuality(item)
               item.sell_in = self.updateItemsell_in(item);
               if (item.sell_in < 0):
                if (self.isIncreasingQualityItem(item)):
                    item.quality = 0
                if (self.isDecreasingQualityItem(item)):
                    item.quality = self.degradeQuality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
