# -*- coding: utf-8 -*-
import scrapy
from pymongo import MongoClient
from scrapy.utils.project import get_project_settings

from conf_util import ConfUtil
from file_downloader.items import AudioItem


class KlAudioSpider(scrapy.Spider):
    name = "kl_audio"
    client = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())
    db = client[ConfUtil.getDBName()]
    k_audio = db[ConfUtil.getKLAudioCollectionName()]
    custom_settings = get_project_settings().getdict('KL_SETTINGS')
    FILES_STORE_BASE = custom_settings['FILES_STORE']
    k_audio_collection_name = ConfUtil.getKLAudioCollectionName()

    start_urls = (
        'http://www.baidu.com'
    )

    def parse(self, response):
        cursor = self.k_audio.find(
            {
                'audioDownloadDir':None
            }
        )
        for audio in cursor:
            audioItem = AudioItem()
            audioItem['_id'] = audio['_id']
            audioItem['collection'] = self.k_audio_collection_name
            audioItem['url'] = audio['m3u8PlayUrl']
            audioItem['audio_base'] = self.FILES_STORE_BASE
            yield audioItem

