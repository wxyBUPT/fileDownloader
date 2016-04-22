# -*- coding: utf-8 -*-

import os.path
import scrapy
from scrapy.pipelines.files import FilesPipeline
from pymongo import MongoClient
from conf_util import ConfUtil
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FileDownloaderPipeline(object):
    def process_item(self, item, spider):
        return item

class AudioDownloader(FilesPipeline):
    client = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())
    db = client[ConfUtil.getDBName()]

    def get_media_requests(self, item, info):
        yield scrapy.Request(item['url'])

    def item_completed(self, results, item, info):
        '''
        文件已经下载完毕，需要将文件的路径保存在mongo 中
        :param results:
        :param item:
        :param info:
        :return:
        '''
        '''
        results 的形式如下
        [(True, {'url': 'http://audio.xmcdn.com/group8/M04/37/6C/wKgDYVb_iwyzAqwqABd42Fth8jI393.m4a',
        'path': 'full/9668aa9324060a7d8e193b46b96257.m4a',
        'checksum': '79b63c45bef51ebac3aa5ab69018d0d9'})]
        '''
        path = os.path.join(item['audio_base'],results[0][1]['path'])
        checksum = results[0][1]['checksum']
        print item['_id']
        print item['collection']

        self.db[item['collection']].update(
            {'_id':item['_id']},
            {
                '$set':{
                    'audioDownloadDir':path,
                    'checksum':checksum
                }
            }
        )



