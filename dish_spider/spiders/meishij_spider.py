# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from dish_spider.items import DishItem

class MeishijSpider(CrawlSpider):
    name = "meishij"
    allowed_domains = ["meishij.net"]
    start_urls = [
        'http://www.meishij.net/chufang/diy/jiangchangcaipu/',
    ]
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('diy/langcaipu/', ), deny=('subsection', ), follow=True)),
        Rule(LinkExtractor(allow=('diy/langcaipu/', )), callback='parse_item'),
    )

    category_dict = dict()
    category_dict['langcaipu'] = '凉菜'
    category_dict['jiangchangcaipu'] = '家常菜'
    category_dict['haixian'] = '海鲜'
    category_dict['tangbaocaipu'] = '汤粥'
    category_dict['sushi'] = '素食'
    category_dict['jiangliaozhanliao'] = '酱料'
    category_dict['huoguo'] = '火锅'
    category_dict['tianpindianxin'] = '甜品点心'
    category_dict['gaodianxiaochi'] = '糕点主食'
    category_dict['ganguo'] = '干果'
    category_dict['rujiangcai'] = '酱卤'
    category_dict['yinpin'] = '饮品'

    def parse_item(self, response):
        pinyin_arr = response.url.split('/')
        category = pinyin_arr[-1] if pinyin_arr[-1] != '' else pinyin_arr[-2]
        category = self.category_dict[category]
        for cell in response.xpath('//div[@class="listtyle1"]/a/div/div/div/strong/text()'):
            dish = DishItem()
            dish['category'] = category
            dish['cuisine'] = ''
            dish['name'] = cell.extract()
            yield dish