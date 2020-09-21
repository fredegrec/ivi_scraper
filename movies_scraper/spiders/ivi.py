# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from movies_scraper.items import MovieItem

MOVIES_QUERY = (
    'https://www.ivi.ru/movies/all'
)


class IviSpider(CrawlSpider):
    name = 'ivi'
    allowed_domains = ['ivi.ru']
    start_urls = [MOVIES_QUERY]

    rules = (Rule(
        LinkExtractor(allow=r'^https://www.ivi.ru/watch/\d+',
                      deny=r'^https://www.ivi.ru/watch/\d+/'),
        follow=True,
        callback='parse_movie',
    ),)

    def parse_movie(self, response):
        item_loader = ItemLoader(item=MovieItem(), response=response)
        item_loader.add_xpath('title',
                              '//li[@class="breadCrumbs__item"]/span/text()')
        item_loader.add_xpath('description',
                              '//p/text()')
        item_loader.add_xpath('languages',
                              '//div[@class="filmOption__value"]/text()')
        item_loader.add_xpath('rating',
                              '//div[@class="nbl-ratingAmple__value"]/span/text()')
        item_loader.add_xpath('scores',
                              '//div[@class="nbl-progressBar__valueBar"]/@style')
        parameters = response.xpath(
                              '//div[@class="parameters__info"]/a/text()').extract()
        item_loader.add_value('year',
                              parameters[0])
        item_loader.add_value('country',
                              parameters[1])
        item_loader.add_value('genres',
                              parameters[2:])
        item_loader.add_xpath('duration',
                              '//div[@class="iconedText__title/text()"]')
        item_loader.add_xpath('people',
                              '//div[@class="fixedSlimPosterBlock__textSection"]/div/text()')
        item_loader.add_xpath('film_lists',
                              '//li[@class="suggestion__item"]/a/text()')

        yield item_loader.load_item()