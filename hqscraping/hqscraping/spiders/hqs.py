import scrapy
import time

class HqsSpider(scrapy.Spider):
    name = 'hqs'
    start_urls = ['https://baixarquadrinhos.com/page/1/']

    def parse(self, response):
        for hq in response.css('.product'):
            yield {
                
                #response.css('.product').get()  
               "titulo" : hq.css('.woocommerce-loop-product__title::text').get() ,
                "readmore" : hq.css('.product_type_simple ::attr(href)').get()   
            }
        prox_page = response.css('.next::attr(href)').get()
        if prox_page is not None:
            prox_page = response.urljoin(prox_page)
            yield scrapy.Request(prox_page, callback=self.parse)
            

           