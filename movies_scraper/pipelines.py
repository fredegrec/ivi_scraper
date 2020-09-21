# -*- coding: utf-8 -*-

from movies_scraper.tools import grouper


class IviItemPipeline(object):
    def process_item(self, item, spider):
        item['rating'] = ''.join(item['rating'])
        item['scores'] = [x.split(':')[-1] for x in item['scores']]
        item['people'] = list(grouper(item['people'], 3))
        return item
