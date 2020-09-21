# -*- coding: utf-8 -*-

BOT_NAME = 'movies_scraper'

SPIDER_MODULES = ['movies_scraper.spiders']
NEWSPIDER_MODULE = 'movies_scraper.spiders'

ITEM_PIPELINES = {
    'movies_scraper.pipelines.IviItemPipeline': 100,
}

# Saving the output in json format
FEED_URI = 'data/%(name)s.json'
FEED_FORMAT = 'json'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True
