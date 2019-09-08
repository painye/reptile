# -*- coding: utf-8 -*-
import scrapy

from quotetutoriol.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    # 解析爬取请求
    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            text = quote.css(".text::text").extract_first()
            author = quote.css(".author::text").extract_first()
            tags = quote.css(".tags .tag::text").extract()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        next = response.css(".pager .next a::attr(href)").extract_first()
        # next的URL补全
        url = response.urljoin(next)
        # parse 回调自己
        yield scrapy.Request(url=url, callback=self.parse)