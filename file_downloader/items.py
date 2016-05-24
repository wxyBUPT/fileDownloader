# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FileDownloaderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class AudioItem(scrapy.Item):
    type = 'audio'
    #对应的collection
    collection = scrapy.Field()
    #数据库中对应的id
    _id = scrapy.Field()
    #发送请求的url
    url = scrapy.Field()
    #文件存储路径
    audio_base = scrapy.Field()

class LiveImageItem(scrapy.Item):
    type = 'live'
    #对应的collection
    collection = scrapy.Field()
    #数据库中对应的_id
    _id = scrapy.Field()
    #发送请求的url
    url = scrapy.Field()
    #文件存储的路径
    image_base = scrapy.Field()
