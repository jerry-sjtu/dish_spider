# -*- coding: utf-8 -*-
import json
import codecs
from scrapy.exceptions import DropItem
from dish_spider.items import *

class MeishijDishPipeline(object):
    def __init__(self):
        self.file = None

    def process_item(self, item, spider):
        if isinstance(item, DishItem) == False or spider.name != 'meishij_dish':
            return item

        if item == None:
            raise DropItem("Null item error." )

        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        if self.file != None:
            self.file.close()

    def open_spider(self, spider):
        if spider.name == 'meishij_dish':
            self.file = codecs.open('meishij_dish.json', 'w', 'utf-8')


class MeishijMaterialPipeline(object):
    def __init__(self):
        self.file = None

    def process_item(self, item, spider):
        if spider.name != "meishij_material" or isinstance(item, MaterialItem) == False:
            return False

        if item == None:
            raise DropItem("Null item error." )

        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        if self.file != None:
            self.file.close()

    def open_spider(self, spider):
        if spider.name == 'meishij_material':
            self.file = codecs.open('meishij_material.json', 'w', 'utf-8')


