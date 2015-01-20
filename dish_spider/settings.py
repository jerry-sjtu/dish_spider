# -*- coding: utf-8 -*-

# Scrapy settings for dish_spider project
BOT_NAME = 'baidu spider'
USER_AGENT = 'baidu spider (http://www.baidu.com)'

SPIDER_MODULES = ['dish_spider.spiders']
NEWSPIDER_MODULE = 'dish_spider.spiders'
ITEM_PIPELINES = {
    'dish_spider.pipelines.MeishijPipeline': 300,
}

