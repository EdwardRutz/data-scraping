# Loop through a list of provided urls and follow them

import scrapy


class HorseSpider(scrapy.Spider):

    name = 'ike'   # Spider's name

    # Define the initial request to make
    def start_requests(self):
        # URLs to process
        urls = ['https://treehouse-projects.github.io/horse-land/index.html',
                'https://treehouse-projects.github.io/horse-land/mustang.html']

        # return a scrapy list, loop through each url and call parse method
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    # If applicable, how to follow links
    def parse(self, response):
        url = response.url  # scrapy response object
        page = url.split('/')[-1]
        filename = 'horses-%s' % page
        print('URL is: {}' .format(url))

        # Save page
        with open(filename, 'wb') as file:
            file.write(response.body)

        print('Saved file %s')

