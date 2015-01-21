# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from dish_spider.items import MaterialItem

class MeishijMaterialSpider(CrawlSpider):
    name = "meishij_material"
    allowed_domains = ["meishij.net"]
    start_urls = [
        'http://www.meishij.net/shicai/shucai_list',
        'http://www.meishij.net/shicai/shuiguo_list',
        'http://www.meishij.net/shicai/shuleidianfen_list',
        'http://www.meishij.net/shicai/junzao_list',
        'http://www.meishij.net/shicai/xurou_list',
        'http://www.meishij.net/shicai/qinrou_list',
        'http://www.meishij.net/shicai/yuxiaxiebei_list',
        'http://www.meishij.net/shicai/danlei_list',
        'http://www.meishij.net/shicai/gulei_list',
        'http://www.meishij.net/shicai/gandou_list',
        'http://www.meishij.net/shicai/jianguozhongzi_list',
    ]

    shucai_allow = ('shicai/shucai_list$', 'shicai/shucai_list.page=[0-9]+')
    shuiguo_allow = ('shicai/shuiguo_list$', 'shicai/shuiguo_list.page=[0-9]+')
    shulei_allow = ('shicai/shuleidianfen_list$', 'shicai/shuleidianfen_list.page=[0-9]+')
    junzao_allow = ('shicai/junzao_list$', 'shicai/junzao_list.page=[0-9]+')
    xurou_allow = ('shicai/xurou_list$', 'shicai/xurou_list.page=[0-9]+')
    qinrou_allow = ('shicai/qinrou_list$', 'shicai/qinrou_list.page=[0-9]+')
    yuxia_allow = ('shicai/yuxiaxiebei_list$', 'shicai/yuxiaxiebei_list.page=[0-9]+')
    danlei_allow = ('shicai/danlei_list$', 'shicai/danlei_list.page=[0-9]+')
    gulei_allow = ('shicai/gulei_list$', 'shicai/gulei_list.page=[0-9]+')
    gandou_allow = ('shicai/gandou_list$', 'shicai/gandou_list.page=[0-9]+')
    jianguo_allow = ('shicai/jianguozhongzi_list$', 'shicai/jianguozhongzi_list.page=[0-9]+')

    rules = (
        Rule(LinkExtractor(allow=shucai_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=shuiguo_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=shulei_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=junzao_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=xurou_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=qinrou_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=yuxia_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=danlei_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=gulei_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=gandou_allow, deny=()), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=jianguo_allow, deny=()), callback='parse_item', follow=True),
    )

    category_dict = dict()
    category_dict['shucai_list'] = u'蔬菜'
    category_dict['shuiguo_list'] = u'水果'
    category_dict['shuleidianfen_list'] = u'薯类淀粉'
    category_dict['junzao_list'] = u'菌藻'
    category_dict['xurou_list'] = u'畜肉'
    category_dict['qinrou_list'] = u'禽肉'
    category_dict['yuxiaxiebei_list'] = u'鱼虾蟹贝'
    category_dict['danlei_list'] = u'蛋类'
    category_dict['gulei_list'] = u'谷类'
    category_dict['gandou_list'] = u'干豆'
    category_dict['jianguozhongzi_list'] = u'坚果种子'


    def parse_item(self, response):
        i = response.url.find('?')
        url = response.url if i < 0 else response.url[0:i]
        pinyin_arr = url.split('/')
        category = pinyin_arr[-1] if pinyin_arr[-1] != '' else pinyin_arr[-2]
        category = self.category_dict[category]
        for cell in response.xpath('//div[@class="listtyle1"]/div[@class="info1"]'):
            item = MaterialItem()
            item['category'] = category
            if len(cell.xpath('div/span/text()')) > 0:
                item['desc'] = cell.xpath('div/span/text()')[0].extract()
            if len(cell.xpath('h3/a/text()')) > 0:
                item['name'] = cell.xpath('h3/a/text()')[0].extract()
            yield item