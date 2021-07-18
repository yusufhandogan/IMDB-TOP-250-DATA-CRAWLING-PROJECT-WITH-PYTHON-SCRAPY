import scrapy
from IMDB.items import ImdbItem
from scrapy.loader import ItemLoader


class PROJECT_IMDB(scrapy.Spider):

    name = "IMDBSPIDER"

    def start_requests(self):

        urls = ["https://www.imdb.com/chart/top/"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        items = ImdbItem()

        all_movies = response.css("tr")

        for movie in all_movies:

            MOVIE_CODE = movie.xpath(
                "//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr[1]/td[2]/a/@href").extract_first()[9:16]

            MOVIE_NAME = response.css("td.titleColumn a::text").extract()

            YEAR = response.css("td.titleColumn a::attr(href)").extract()

            IMDB_RATING =movie.css("td.ratingColumn strong::text").extract()

        
        
        items["MOVIE_CODE"] = MOVIE_CODE

        items["MOVIE_NAME"] = MOVIE_NAME

        items["YEAR"] = YEAR

        items["RANK"] = RANK

        items["IMDB_RATING"] = IMDB_RATING

        yield items
