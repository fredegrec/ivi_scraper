# -*- coding: utf-8 -*-

import scrapy
from scrapy.loader.processors import TakeFirst


class MovieItem(scrapy.Item):
    title = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field()
    languages = scrapy.Field(output_processor=TakeFirst())
    rating = scrapy.Field()
    scores = scrapy.Field()
    year = scrapy.Field()
    country = scrapy.Field()
    genres = scrapy.Field()
    duration = scrapy.Field(output_processor=TakeFirst())
    people = scrapy.Field()
    film_lists = scrapy.Field()
