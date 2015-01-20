# -*- coding: utf-8 -*-
import scrapy

class DishItem(scrapy.Item):
    category = scrapy.Field()
    cuisine = scrapy.Field()
    name = scrapy.Field()

        