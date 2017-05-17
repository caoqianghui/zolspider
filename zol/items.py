# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZolPhoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    p_url = scrapy.Field()
    
    parms_1 = scrapy.Field()
    parms_2 = scrapy.Field()
    parms_3 = scrapy.Field()
    parms_4 = scrapy.Field()
    parms_5 = scrapy.Field()
    parms_6 = scrapy.Field()
    parms_7 = scrapy.Field()