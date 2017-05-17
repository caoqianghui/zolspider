# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from zol.items import ZolPhoneItem

base_url = "http://detail.zol.com.cn"

class ZolspiderSpider(scrapy.Spider):
    name = "zolspider"
    allowed_domains = ["detail.zol.com.cn"]
    start_urls = ['http://detail.zol.com.cn/cell_phone_index/subcate57_list_1.html']
    
    first_url_list = []
    
    def parse(self, response):
        first_url_list = response.xpath('//*[@id="J_PicMode"]/li/a/@href').extract()
        for list in first_url_list:
            phone_url = base_url + str(list)
            yield Request(phone_url, callback=self.parse_first_page, dont_filter=True)
        next_page = ''.join(response.xpath('//div[contains(@class, "pagebar")]/a[contains(@class,"next")]/@href').extract())
        if next_page:
            next_url = base_url + str(next_page)
            yield Request(next_url, callback=self.parse, dont_filter=True)
    
    def parse_first_page(self, response):
        item = ZolPhoneItem()
        item['title'] = ''.join(response.xpath('//div[contains(@class, "page-title clearfix")]/h1/text()').extract()).encode('utf-8')
        item['price'] = ''.join(response.xpath('//*[@id="J_PriceTrend"]/b[2]/text()').extract()).encode('utf-8')
        item['p_url'] = response.url
        param_list_url = ''.join(response.xpath('//ul[contains(@class,"nav")]/li/a[contains(@href, "param")]/@href').extract())
        param_url = base_url + str(param_list_url)
        request = Request(param_url, callback=self.parse_second_page)
        request.meta['item'] = item
        yield request

    def parse_second_page(self, response):
        item = response.request.meta['item']
        item['parms_1'] = ''.join(response.xpath('//div[contains(@class,"param-table")]/table[1]//text()[normalize-space(.)]').extract()).encode('utf-8')
        item['parms_2'] = ''.join(response.xpath('//div[contains(@class,"param-table")]/table[2]//text()[normalize-space(.)]').extract()).encode('utf-8')
        item['parms_3'] = ''.join(response.xpath('//div[contains(@class,"param-table")]/table[3]//text()[normalize-space(.)]').extract()).encode('utf-8')
        item['parms_4'] = ''.join(response.xpath('//div[contains(@class,"param-table")]/table[4]//text()[normalize-space(.)]').extract()).encode('utf-8')
        item['parms_5'] = ''.join(response.xpath('//div[contains(@class,"param-table")]/table[5]//text()[normalize-space(.)]').extract()).encode('utf-8')
        item['parms_6'] = ''.join(response.xpath('//div[contains(@class,"param-table")]/table[6]//text()[normalize-space(.)]').extract()).encode('utf-8')
        item['parms_7'] = ''.join(response.xpath('//div[contains(@class,"param-table")]/table[7]//text()[normalize-space(.)]').extract()).encode('utf-8')
        yield item
        
        