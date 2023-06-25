# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义数据模型  ： 明确抓取数据

class ScrspydemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    name = scrapy.Field()

    title = scrapy.Field()

    desc = scrapy.Field()




    pass
