# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbItem(scrapy.Item):

    MOVIE_CODE = scrapy.Field()
    
    MOVIE_NAME = scrapy.Field()
    
    YEAR = scrapy.Field()

    RANK = scrapy.Field()
    
    IMDB_RATING = scrapy.Field()

    