# -*- coding: utf-8 -*-
import os
import scrapy
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

from conf_util import ConfUtil
from file_downloader.items import AudioItem

class XmlyAudioSpider(scrapy.Spider):
    name = "xmly_audio"
    start_urls = (

    )
    client = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())
    db = client[ConfUtil.getDBName()]
    c_audio = db[ConfUtil.getXMLYAudioCollectionName()]
    custom_settings = get_project_settings().getdict('XMLY_SETTINGS')
    FILES_STORE_BASE = custom_settings['FILES_STORE']

    def start_requests(self):
        yield scrapy.Request(
            'http://www.baidu.com',callback=self.parse
        )

    def parse(self,response):
        cursor = self.c_audio.find(
            {
               'audioDownloadDir':None
            }
        )
        for audio in cursor:
            audioItem = AudioItem()
            audioItem['_id'] = audio['_id']
            audioItem['collection'] = 'xmly_audio'
            audioItem['url'] = audio['play_path']
            audioItem['audio_base'] = self.FILES_STORE_BASE
            yield audioItem
