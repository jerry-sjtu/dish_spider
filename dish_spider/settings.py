# -*- coding: utf-8 -*-

# Scrapy settings for dish_spider project
BOT_NAME = 'dish_spider'
USER_AGENT = 'dish_spider (+http://www.yourdomain.com)'

SPIDER_MODULES = ['dish_spider.spiders']
NEWSPIDER_MODULE = 'dish_spider.spiders'
ITEM_PIPELINES = {
    'dish_spider.pipelines.MeishijPipeline': 300,
}

