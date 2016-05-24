#coding=utf-8
import scrapy
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

from conf_util import ConfUtil
from file_downloader.items import LiveImageItem
__author__ = 'xiyuanbupt'

class LiveImageSpider(scrapy.Spider):
    name = "live_image"
    client = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())
    db = client[ConfUtil.getLiveDbName()]
    live_coll = db[ConfUtil.getLiveCollectionName()]
    custom_settings = get_project_settings().getdict('LIVE_SETTINGS')
    FILES_STORE_BASE = custom_settings['FILES_STORE']

    live_coll_name = ConfUtil.getLiveCollectionName()

    start_urls = (
    )

    def start_requests(self):
        yield scrapy.Request(
            'http://www.baidu.com',callback=self.parse
        )

    def parse(self, response):
        cursor = self.live_coll.find(
            {
                'img':{
                    "$exists":False
                }
            }
        )
        for live in cursor:
            liveItem = LiveImageItem()
            liveItem['_id']=live['_id']
            liveItem['collection'] = self.live_coll_name
            liveItem['url'] = live['imgSrc']
            liveItem['image_base'] = self.FILES_STORE_BASE
            yield liveItem
