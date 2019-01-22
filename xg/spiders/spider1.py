# -*- coding: utf-8 -*-
import csv
import json

import scrapy
from scrapy import Request
from xg.items import XgItem


class Spider1Spider(scrapy.Spider):
    name = 'spider1'

    start_urls = ['http://www.lefeng.com/']
    def parse(self, response):
        lis = response.xpath("//div[@class='brand-item']")
        for li in lis:
            title = li.xpath('./a/@title').extract()[0]
            url = li.xpath('./a/@href').extract()[0]
            print(url,title)
            num = url[-14:-5]
            for i in range(1, 5):
                url = 'http://brand.lefeng.com/ajax/showMoreData?brandId=' + num + '&limit=12&sort=&page' + str(i)
                # resp = Request(url)
                # a = json.loads(response.text)
                # lis = a['data']
                # print(response.url)
                # if len(lis) > 5:
                #     print(response.url)
                yield Request(url,callback=self.brand)

    def brand(self, response):
        #a = response.body.encoding='utf-8'
        a = json.loads(response.text)
        item = XgItem
        lis = a['data']

        if len(lis)> 5:

            for li in lis:
                brandStoreName = li['goods']['brandStoreName']
                name = li['goods']['name']
                marketPrice = li['goods']['marketPrice']
                agio = li['goods']['agio']
                vipshopPrice = li['goods']['vipshopPrice']
                img = li['goods']['image']
                allimg = li['goods']['allImages']
                #print([brandStoreName,name,marketPrice,agio,vipshopPrice,img])

                item = XgItem(brandStoreName=brandStoreName,
                              name=name,
                              marketPrice=marketPrice,
                              agio=agio,
                              vipshopPrice=vipshopPrice,
                              img=img)
                yield item





