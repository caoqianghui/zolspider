# -*- coding: utf-8 -*-

import scrapy
from scrapy.exceptions import DropItem
from twisted.enterprise import adbapi
import MySQLdb.cursors
from scrapy import log

class ZolPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', host='localhost', db='zol',\
                user='root', passwd='rootroot', cursorclass=MySQLdb.cursors.DictCursor,\
                charset='utf8', use_unicode=True)
        if self.dbpool:
            log.msg("connetc sucess")
        else:
            log.msg("connetc faild")
    def process_item(self, item, spider):
        if item['price']:
            query = self.dbpool.runInteraction(self._conditional_insert, item)
            return item
        else:
            raise DropItem("miss price %s " %item['price'])
        
    def _conditional_insert(self, tx, item):
        tx.execute(
            "insert into zolphone (title, price, product_url,par_1,par_2,par_3,par_4,par_5,par_6,par_7)"
            " values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (item['title'],item['price'],item['p_url'],item['parms_1'], item['parms_2'],
            item['parms_3'], item['parms_4'], item['parms_5'], item['parms_6'], item['parms_2'])
            )
        log.msg("Item stored in db: %s" % item['title'], level=log.DEBUG)