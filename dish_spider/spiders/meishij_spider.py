# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from dish_spider.items import DishItem

class MeishijSpider(CrawlSpider):
    name = "meishij"
    allowed_domains = ["meishij.net"]
    start_urls = [
        'http://www.meishij.net/chufang/diy/jiangchangcaipu/',
        'http://www.meishij.net/chufang/diy/haixian/',
        'http://www.meishij.net/chufang/diy/tangbaocaipu/',
        'http://www.meishij.net/chufang/diy/sushi/',
        'http://www.meishij.net/chufang/diy/jiangliaozhanliao/',
        'http://www.meishij.net/chufang/diy/huoguo/',
        'http://www.meishij.net/chufang/diy/tianpindianxin/',
        'http://www.meishij.net/chufang/diy/gaodianxiaochi/',
        'http://www.meishij.net/chufang/diy/ganguo/',
        'http://www.meishij.net/chufang/diy/rujiangcai/',
        'http://www.meishij.net/chufang/diy/yinpin/',
    ]

    liangcai_allow = ('chufang/diy/langcaipu/$', 'chufang/diy/langcaipu/.&page=[0-9]+',)
    #liangcai_allow = ('chufang/diy/langcaipu/$',)
    liangcai_deny = ('chufang/diy/langcaipu/[0-9]+.html',) 
    haixian_allow = ('chufang/diy/haixian/$', 'chufang/diy/haixian/.&page=[0-9]+')
    haixian_deny = ('chufang/diy/haixian/[0-9]+.html',) 
    tangbao_allow = ('chufang/diy/tangbaocaipu/$', 'chufang/diy/tangbaocaipu/.&page=[0-9]+')
    tangbao_deny = ('chufang/diy/tangbaocaipu/[0-9]+.html',) 
    sushi_allow = ('chufang/diy/sushi/$', 'chufang/diy/sushi/.&page=[0-9]+')
    sushi_deny = ('chufang/diy/sushi/[0-9]+.html',) 
    jiangliao_allow = ('chufang/diy/jiangliaozhanliao/$', 'chufang/diy/jiangliaozhanliao/.&page=[0-9]+')
    jiangliao_deny = ('chufang/diy/jiangliaozhanliao/[0-9]+.html',) 
    huoguo_allow = ('chufang/diy/huoguo/$', 'chufang/diy/huoguo/.&page=[0-9]+')
    huoguo_deny = ('chufang/diy/huoguo/[0-9]+.html',) 
    tianpin_allow = ('chufang/diy/tianpindianxin/$', 'chufang/diy/tianpindianxin/.&page=[0-9]+')
    tianpin_deny = ('chufang/diy/tianpindianxin/[0-9]+.html',)
    gaodianxiaochi_allow = ('chufang/diy/gaodianxiaochi/$', 'chufang/diy/gaodianxiaochi/.&page=[0-9]+')
    gaodianxiaochi_deny = ('chufang/diy/gaodianxiaochi/[0-9]+.html',)
    ganguo_allow = ('chufang/diy/ganguo/$', 'chufang/diy/ganguo/.&page=[0-9]+')
    ganguo_deny = ('chufang/diy/ganguo/[0-9]+.html',)
    jianlu_allow = ('chufang/diy/rujiangcai/$', 'chufang/diy/rujiangcai/.&page=[0-9]+')
    jianlu_deny = ('chufang/diy/rujiangcai/[0-9]+.html',)
    yinpin_allow = ('chufang/diy/yinpin/$', 'chufang/diy/yinpin/.&page=[0-9]+')
    yinpin_deny = ('chufang/diy/yinpin/[0-9]+.html',)

    rules = (
        Rule(LinkExtractor(allow=liangcai_allow, deny= liangcai_deny), callback='parse_item', follow=True),
        #Rule(LinkExtractor(allow=('chufang/diy/langcaipu/',), deny= liangcai_deny), callback='parse_item'),
        Rule(LinkExtractor(allow=haixian_allow, deny= haixian_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=tangbao_allow, deny= susi_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=susi_allow, deny= tangbao_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=jiangliao_allow, deny= jiangliao_allow), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=huoguo_allow, deny= huoguo_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=tianpin_allow, deny= tianpin_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=gaodianxiaochi_allow, deny= gaodianxiaochi_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=ganguo_allow, deny= ganguo_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=jianlu_allow, deny= jianlu_deny), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=yinpin_allow, deny= yinpin_deny), callback='parse_item', follow=True),
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