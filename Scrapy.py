##############
# Import scrapy
##############
import scrapy


class Extract(scrapy.spiders):
    name = 'Spider'
    start_urls = ['http://192.168.186.141/spicyx']

    def parse(self, response):
        # Extract 'img'
        Image_selector = 'img'

        for x in response.css(Image_selector):
            # Image stored in src attribute
            newsel = '@src'

            # Show image url
            yield {
                'Image Link:': x.xpath(newsel).extract_first(),
            }

        # Recursing next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request (
                response.urljoin(next_page),
                callback=self.parse
            )
