# -*- coding: utf-8 -*-
import scrapy


class DealSpider(scrapy.Spider):
    name = 'deal'
    allowed_domains = ['www.groupon.com']
    start_urls = ['https://www.groupon.com/landing/deal-of-the-day']

    def parse(self, response):
        products = response.xpath("//div[@class='grpn-dc-caption']")

        for product in products:
            yield{
                "title" : product.xpath(".//div[@class='grpn-dc-title']/text()").get(),
                "price" : product.xpath(".//span[@class='wh-dc-price-regular']/text()").get(),
                "rank" : product.xpath(".//div[@class='grpn-total-ratings']/text()").get()
            }
