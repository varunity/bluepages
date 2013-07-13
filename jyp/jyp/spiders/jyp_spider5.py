from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from jyp.items import JypItem


class JypSpider(BaseSpider):
    name = "jyp5"
    allowed_domains = ["http://s2.jamaicayp.com"]
    start_urls = [
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/1/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/2/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/3/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/4/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/5/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/6/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/7/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/8/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/9/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/10/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/11/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/12/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/13/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/14/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/15/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/16/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/17/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/18/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/19/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/20/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/21/book",
        "http://s2.jamaicayp.com/Jamaica-Kingston/Government/22/book"
    ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)	
        div1 = hxs.select('.//form[@name=\'vform\']/div/div')
        nums = div1.select('//div[not(@id) and not(@class)]/span[3]/span[3]/span/span[@class=\'WBP\']')
        infos = []
        for each in nums:
            upsibs = each.select('./preceding-sibling::span')
            info = JypItem()
            info['ghn'] = upsibs.select('.//span[@class=\'GHN\']/text()').extract()
            info['gel'] = upsibs.select('self::*[@class=\'GEL\']/text()').extract()
            info['wbp'] = each.select('text()').extract()
            info['wadak'] = upsibs.select('self::*[@class=\'WAD AK\']/text()').extract()
            info['wp'] = upsibs.select('self::*[@class=\'WP\']/text()').extract()
            info['wad'] = upsibs.select('self::*[@class=\'WAD\']/text()').extract()
            info['wbn'] = upsibs.select('self::*[@class=\'WBN\']/text()').extract()
            info['wn'] = upsibs.select('self::*[@class=\'WN\']/text()').extract()
            infos.append(info)
        return infos
	
