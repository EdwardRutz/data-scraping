# A spider to scrape a form using scrapy

from scrapy.http import FormRequest
from scrapy.spiders import Spider

# Create a new class that inherits from Spider
class FormSpider(Spider):
    name = 'horseForm'

    # Define start url
    start_urls = ['https://treehouse-projects.github.io/horse-land/form']

    # Define parse method and the data to pass in
    def parse(self, response):
        formdata = {}

        # Identify form fields and provide data
        formdata = {'firstname': 'Speed',
                    'lastname': 'Racer',
                    'jobtitle': 'NASCAR'}

        # Return a form request from Response object
        return FormRequest.from_response(response, formnumber=0,
                                         formdata=formdata,
                                         callback=self.after_post)

    def after_post(self, response):
        print('\n\n************\nForm processed.\n')
        print(response)
        print('\n********\n')
