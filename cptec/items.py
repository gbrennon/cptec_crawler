# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CptecItem(scrapy.Item):
    date = scrapy.Field()
    weather = scrapy.Field()
    max_temperature = scrapy.Field()
    min_temperature = scrapy.Field()
    uvi = scrapy.Field()
