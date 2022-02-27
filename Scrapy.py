##############
# Import scrapy
##############
import scrapy

##############
#Class Extract
##############
class Extract(scrapy.spiders):
    #Name for scrapy
    name = 'Spider'

    #Website input
    start_urls = ['http://192.168.186.141/spicyx']

    #############################
    #Parse function
    #Start crawling website
    #############################
    def parse(self, response):
        # Extract image with 'img' tag
        Image_selector = 'img'

        #Loop response to extract each image URL
        for x in response.css(Image_selector):
            # Image stored in src attribute
            URL = '@src'

            # Display image url
            yield {
                'Image Link:': x.xpath(URL).extract_first(),
            }
        #####################
        #To recurse next page
        #####################
        #Select '.next a' tag with 'href' attribute
        Page_selector = '.next a ::attr(href)'

        #Extract URL to next page
        next_page = response.css(Page_selector).extract_first()

        #If valid URL is avaliable, follow link call Parse function on the link
        if next_page:
            yield scrapy.Request (
                response.urljoin(next_page),
                callback=self.parse
            )