# A spider to extract links from a site and follow them

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# Define class and inherit from CrawlSpider
class HorseSpider(CrawlSpider):
    name = 'whirlaway'

    allowed_domains = ['treehouse-projects.github.io']
    start_urls = ['http://treehouse-projects.github.io/horse-land']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_horses',
                  follow=True)]

    def parse_horses(self, response):
        url = response.url
        title = response.css('title::text').extract()
        print('Page URL: {}'.format(url))
        print('Page title: {}'.format(title))
