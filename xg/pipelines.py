import csv
from logging import log

import pymysql.cursors


class XgPipeline(object):
    def __init__(self):
        print('开始连接')
        self.connect = pymysql.connect(
            host='localhost',
            user='root',
            passwd='123456',
            db='xg',
            charset='utf8')
        self.cursor = self.connect.cursor()
        print('连接成功')


    def process_item(self, item, spider):

        brandStoreName = item['brandStoreName']
        name = item['name']
        marketPrice = item['marketPrice']
        agio = item['agio']
        vipshopPrice = item['vipshopPrice']
        img = item['img']
        #allimg = item['allimg']
        print(brandStoreName, name, marketPrice, agio, vipshopPrice, img)
        # allimg = item.get("allimg", "N/A")
        try:
            sql = "insert into project (brandStoreName,name,marketPrice,agio,vipshopPrice,img) value(%s, %s, %s,%s, %s, %s)"
            print('存储成功')
            self.cursor.execute(sql, (brandStoreName, name, marketPrice, agio, vipshopPrice, img))
            self.connect.commit()
        except Exception as error:
            log(error)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()

