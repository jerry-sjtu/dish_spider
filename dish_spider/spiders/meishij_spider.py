# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from dish_spider.items import DishItem

class MeishijSpider(CrawlSpider):
    name = "meishij"
    allowed_domains = ["meishij.net"]
    start_urls = [
        'http://www.meishij.net/chufang/diy/jiangchangcaipu/?&page=1',
    ]
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('chufang/diy/langcaipu/\?&page=[0-9]+',),)),
        Rule(LinkExtractor(allow=('chufang/diy/langcaipu/\?&page=[0-9]+',)), callback='parse_item'),
    )

    category_dict = dict()
    category_dict['langcaipu'] = u'凉菜'
    category_dict['jiangchangcaipu'] = u'家常菜'
    category_dict['haixian'] = u'海鲜'
    category_dict['tangbaocaipu'] = u'汤粥'
    category_dict['sushi'] = u'素食'
    category_dict['jiangliaozhanliao'] = u'酱料'
    category_dict['huoguo'] = u'火锅'
    category_dict['tianpindianxin'] = u'甜品点心'
    category_dict['gaodianxiaochi'] = u'糕点主食'
    category_dict['ganguo'] = u'干果'
    category_dict['rujiangcai'] = u'酱卤'
    category_dict['yinpin'] = u'饮品'

    def parse_item(self, response):
        i = response.url.find('?')
        url = response.url if i < 0 else response.url[0:i]
        pinyin_arr = url.split('/')
        category = pinyin_arr[-1] if pinyin_arr[-1] != '' else pinyin_arr[-2]
        category = self.category_dict[category]
        for cell in response.xpath('//div[@class="listtyle1"]/a/div/div/div/strong/text()'):
            dish = DishItem()
            dish['category'] = category
            dish['cuisine'] = ''
            dish['name'] = cell.extract()
            yield dish