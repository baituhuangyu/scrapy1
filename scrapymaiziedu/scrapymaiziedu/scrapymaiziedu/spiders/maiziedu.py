# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item
from scrapymaiziedu.items import MaizieduItem
import re
class maizieduSpider(CrawlSpider):
    name = "Scrapymaiziedu"
    allowed_domains = ["maiziedu.com"]
    start_urls = [
        'http://www.maiziedu.com'
    ]

    rules = [
        Rule(SgmlLinkExtractor(allow=('/html/body/div/header/div/div[2]', )), callback='title_scrapy_page'),

    ]

    def title_scrapy_page(self, response):
        self.log("Fetch page url: %s" % response.url)

        hxs = HtmlXPathSelector(response)
        item = ScrapymaizieduItem()
        pageName = sel.xpath('/html/head/title/text()').extract()
        item['pageName'] = pageName[0]
        courseName = divRootPath.xpath('ul/li[2]/a/text()').extract()
        item['courseName'] = courseName[0]
        courseURL = divRootPath.xpath('ul/li[2]/a/@href').extract()
        item['courseURL'] = courseURL[0]
        print pageName[0]
        return item
    

##    def parse(self, response):
##        sel = Selector(response)
####        pageTitle = sel.xpath('/html/head/title/text()').extract()
####        pageTitlekeywords = sel.xpath('/html/head/meta[@name="keywords"]/@content').extract() ##
####        textfile = open(r'C:\Users\hy\Desktop\scrapy1\scrapymaiziedu\scrapymaiziedu\test.txt','a')
####        textfile.write('pageTitle : %s \r\npageTitlekeywords: %s' % (pageTitle[0].encode('gbk'), pageTitlekeywords[0].encode('gbk')))
####        textfile.close()
####        print pageTitle[0]
##        divRootPath = sel.xpath('/html/body/div/header/div/div[2]')
##        courseName = divRootPath.xpath('ul/li[2]/a/text()').extract()
##        courseURL = divRootPath.xpath('ul/li[2]/a/@href').extract()
##        
##        courseURL1 =r'http://www.maiziedu.com' + courseURL[0]
##        textfile = open(r'C:\Users\hy\Desktop\scrapy1\scrapymaiziedu\scrapymaiziedu\test.txt','a')
##        textfile.write('\r\ncourseName : %s \r\ncourseURL: %s' % (courseName[0].encode('gbk'), courseURL1.encode('gbk')))
##        textfile.close()
##        print courseName[0]
        


    
 

