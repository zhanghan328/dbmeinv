# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import scrapy.selector
from scrapy.http.request import Request
from dbmeinv.items import DbmeinvItem
from dbmeinv.settings import *
class dbmeinv(scrapy.Spider):
    name = 'dbmeinv'
    allowed_domain = ['dbmeinv.com']
    start_urls = ['http://www.dbmeinv.com/dbgroup/show.htm?cid=6']
    def __init__(self):
        self.headers = HEADER

    def parse(self,response):
        sel = response.xpath('//img[@class="height_min"]')
        items = []
        for i in sel:
            item = DbmeinvItem()
            item['image_urls'] = i.xpath('@src').extract()
            yield item
        next_page = response.xpath('//li[@class="next next_page"]/a/@href').extract()
        yield Request('http://www.dbmeinv.com'+next_page[0],headers=self.headers,callback=self.parse)

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url,headers=self.headers,callback=self.parse)
            

