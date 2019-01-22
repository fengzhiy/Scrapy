# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XgItem(scrapy.Item):
    brandStoreName = scrapy.Field()
    name = scrapy.Field()
    marketPrice = scrapy.Field()
    agio = scrapy.Field()
    vipshopPrice = scrapy.Field()
    img = scrapy.Field()



