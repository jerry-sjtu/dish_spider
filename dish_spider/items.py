# -*- coding: utf-8 -*-
import scrapy

class DishItem(scrapy.Item):
    category = scrapy.Field()
    cuisine = scrapy.Field()
    name = scrapy.Field()

class MaterialItem(scrapy.Item):
    category = scrapy.Field()
    name = scrapy.Field()
    desc = scrapy.Field()
        