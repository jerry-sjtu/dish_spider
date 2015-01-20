# -*- coding: utf-8 -*-
import json
import codecs
from scrapy.exceptions import DropItem

class MeishijPipeline(object):
    def __init__(self):
        self.file = codecs.open('meishij.json', 'utf-8', 'wb')

    def process_item(self, item, spider):
        if item == None:
            raise DropItem("Null item error." )
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

    def close_spider(spider):
        self.file.close()

    def open_spider(spider):
        pass