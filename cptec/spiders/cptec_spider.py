import scrapy

from cptec.items import CptecItem


class CptecSpider(scrapy.Spider):
    name = "cptec"
    allowed_domains = ["ctec.inpe.br"]
    start_urls = ["http://servicos.cptec.inpe.br/XML/cidade/242/previsao.xml"]

    def parse(self, response):
        for sel in response.xpath('//cidade/previsao'):
            item = CptecItem()
            item['date'] = sel.xpath('dia/text()').extract()
            item['weather'] = sel.xpath('tempo/text()').extract()
            item['max_temperature'] = sel.xpath('maxima/text()').extract()
            item['min_temperature'] = sel.xpath('minima/text()').extract()
            item['uvi'] = sel.xpath('iuv/text()').extract()
            yield item
