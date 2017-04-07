from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field
from scrapy.cmdline import execute


import string
import time
import csv
import itertools
import unicodedata

'''
    Getting all link Mecial Types
    below code is for retrive link for review one MedicationSamples Types

    PART 1
'''
# class MySpider(BaseSpider):
#     name = "MyScrapperMTSamples"
#     allowed_domains = ["http://mtsamples.com"]
    
#     start_urls=["http://mtsamples.com"]
#     def parse(self,response):
#         hxs = HtmlXPathSelector(response)
#         varlink1 = (hxs.xpath('//div[@id="MenuTypeLeft"]/a/@href').extract())
#         print varlink1
#         result = zip([x.encode('ascii', 'ignore') for x in varlink1])
#         myfile = open('link1.csv', 'a')
#         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#         for row in result:
#             wr.writerow(row)

'''
    PART 2

    Getting all Medical Samples Link
'''
# class MySpider(BaseSpider):
#     name = "MyScrapperMTSamples"
#     allowed_domains = ["http://mtsamples.com"]
    
#     myfile=open("link1.csv")
#     start_urls=[]
#     for row in myfile:
#         start_urls.append("http://mtsamples.com"+row.replace("\r", "").replace("\n", "").replace('"',""))
#     print start_urls
#     def parse(self,response):
#         hxs = HtmlXPathSelector(response)
#         varlink1 = (hxs.xpath('//div[@id="wrapper"]/table/tr/td/div/table[@id="Browse"]/tr/td/a/@href').extract())
#         print varlink1
#         result = zip([x.encode('ascii', 'ignore') for x in varlink1])
#         myfile = open('link3.csv', 'a')
#         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#         for row in result:
#             wr.writerow(row)
'''
    PART 3

    Getting all Medical Trascripts Details
'''
class MySpider(BaseSpider):
    name="MyScrapperMTSamples"
    allowed_domains=["http://mtsamples.com"]

    myfile=open("link2.csv")
    start_urls=["http://mtsamples.com/site/pages/sample.asp?Type=3-Allergy/Immunology&Sample=1428-AllergyEvaluationConsult"]

    def parse(self,response):
        hxs=HtmlXPathSelector(response)
        varlink1=''.join(hxs.select('//table/tr/td/div[@id="sampletext"]//text()').extract())
        varlink1=varlink1.replace('(adsbygoogle = window.adsbygoogle || []).push({});',"").replace("var addthis_config = {\"data_track_clickback\":true};","").replace("View this sample in Blog format on MedicalTranscriptionSamples.com","").replace("|","")
        
        myfile=open("demo.txt","w")
        myfile.write(varlink1)
        myfile.close()

        cleanedLine=[]
        with open("demo.txt", "r") as f:
            for line in f:
                cleanedLine = line.strip()
                if cleanedLine: # is not empty
                    print cleanedLine
                    myfile=open("demo2.txt","a")
                    myfile.write(cleanedLine+'\n')
                    myfile.close()
        # finaldata=''.join((str(e) for e in cleanedLine))
        # print finaldata
