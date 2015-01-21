# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from dish_spider.items import DishItem

class MeishijDishSpider(CrawlSpider):
    name = "meishij_dish"
    allowed_domains = ["meishij.net"]
    start_urls = [
        'http://www.meishij.net/chufang/diy/guowaicaipu1/canqianxiaochi/',
        'http://www.meishij.net/chufang/diy/guowaicaipu1/tangpin/',
        'http://www.meishij.net/chufang/diy/guowaicaipu1/zhucai/',
        'http://www.meishij.net/chufang/diy/guowaicaipu1/zhushi/',
        'http://www.meishij.net/chufang/diy/guowaicaipu1/tiandian/',
    ]

    canqian_allow = ('chufang/diy/guowaicaipu1/canqianxiaochi/$', 'chufang/diy/guowaicaipu1/canqianxiaochi/.&page=[0-9]+')
    canqian_deny = ('chufang/diy/guowaicaipu1/canqianxiaochi/[0-9]+.html',)
    tangpin_allow = ('chufang/diy/guowaicaipu1/tangpin/$', 'chufang/diy/guowaicaipu1/tangpin/.&page=[0-9]+')
    tangpin_deny = ('chufang/diy/guowaicaipu1/tangpin/[0-9]+.html',)
    zhucai_allow = ('chufang/diy/guowaicaipu1/zhucai/$', 'chufang/diy/guowaicaipu1/zhucai/.&page=[0-9]+')
    zhucai_deny = ('chufang/diy/guowaicaipu1/zhucai/[0-9]+.html',)
    zhushi_allow = ('chufang/diy/guowaicaipu1/zhushi/$', 'chufang/diy/guowaicaipu1/zhushi/.&page=[0-9]+')
    zhushi_deny = ('chufang/diy/guowaicaipu1/zhushi/[0-9]+.html',)
    tiandian_allow = ('chufang/diy/guowaicaipu1/tiandian/$', 'chufang/diy/guowaicaipu1/tiandian/.&page=[0-9]+')
    tiandian_deny = ('chufang/diy/guowaicaipu1/tiandian/[0-9]+.html',)

    rules = (
        Rule(LinkExtractor(allow=canqian_allow, deny=canqian_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=tangpin_allow, deny= tangpin_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=zhucai_allow, deny= zhucai_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=zhushi_allow, deny= zhushi_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=tiandian_allow, deny= tiandian_deny), callback='parse_item', follow=True),
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
    category_dict['canqianxiaochi'] = u'餐前小菜'
    category_dict['tangpin'] = u'汤品'
    category_dict['zhucai'] = u'主菜'
    category_dict['zhushi'] = u'主食'
    category_dict['tiandian'] = u'甜点'


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