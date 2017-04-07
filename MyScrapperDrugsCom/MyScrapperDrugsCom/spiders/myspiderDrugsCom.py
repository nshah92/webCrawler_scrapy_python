from scrapy.spiders import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.item import Item, Field

import string
import time
import csv
import time
import unicodedata

''' Store all a-z links to log.text 
    
    i wrote this spider for get the all links of condition from the drugs.com
'''
# class MySpider(BaseSpider):
#     name = "MyScrapperDrugsCom"
#     allowed_domains = ["https://drugs.com/"]
#     start_urls = []
#     start = []
    
#     for i in range(0,26):
#         start_urls.append("https://www.drugs.com/condition/"+string.lowercase[i]+".html")
#     print start

#     def parse(self,response):
#         hxs = HtmlXPathSelector(response)
#         varname=(hxs.xpath('//div[@class="contentBox"]/ul[@class="column-list-2"]/li//a/text()').extract())
#         varlink=(hxs.xpath('//div[@class="contentBox"]/ul[@class="column-list-2"]/li//a/@href').extract())

#         result = zip(varlink)
#         myfile = open('link1.csv', 'a')
#         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
       
#         for i in result:
#             print i
#             wr.writerow(i)
'''
    task -2
'''
# class MySpider(BaseSpider):
#     name = "MyScrapperDrugsCom"
#     allowed_domains = ["https://drugs.com/"]
    
#     myfile=open("link1.csv")
#     start_urls=[]
#     for row in myfile:
#         start_urls.append("https://drugs.com"+row.replace("\r", "").replace("\n", "").replace('"',""))
#     # start_urls.append("https://www.drugs.com/condition/cold-symptoms.html");
#     # print start_urls
 
#     # while True:

#     def parse(self,response):
#         hxs = Selector(response)
#         varDrugReviewLink = (hxs.xpath('//div[@class="contentBox"]/div[@id="conditionBoxWrap"]/table[@class="condition-table"]/tbody/tr[@class="condition-table__summary"]/td[@class="condition-table__reviews"]/a/@href').extract())                       

#         time.sleep(5)  # Delay for 1 minute (60 seconds)

#         print varDrugReviewLink
#         result = zip(varDrugReviewLink)
#         myfile = open('link2.csv', 'a')
#         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
       
#         for i in result:
#             print i
#             wr.writerow(i)
'''
    task - 3
'''
class MySpider(BaseSpider):
    name = "MyScrapperDrugsCom"
    allowed_domains = ["https://drugs.com/"]

    myfile = open("link2.csv")
    start_urls = []

    for row in myfile:
            for i in range(1,20):
                start_urls.append("https://drugs.com"+str(row).replace('"', '').strip()+"?page="+str(i))

    # start_urls.append("https://www.drugs.com/comments/doxycycline/for-acne.html")

    def parse(self,response):
        hxs = Selector(response)
        varDrugName = (hxs.xpath('//div[@class="contentBox"]/h1/text()')).extract()
        varDrugReview = (hxs.xpath('//div[@class="user-comment"]/p[1]/span//text()')).extract()

        # varDrugName = str(varDrugName).replace("User Reviews for","").replace("[","").replace("]","").replace("'","")
        DrugName = [x.encode('ascii', 'ignore') for x in varDrugName]
        # print DrugName[0].replace("User Reviews for","").replace("[","").replace("]","").replace("'","")
        name = list()
        time.sleep(5)
        for j in range(len(varDrugReview)):
            name.append(DrugName[0].replace("User Reviews for","").replace("[","").replace("]","").replace("'","").strip())
        result = zip(name, [x.encode('ascii', 'ignore') for x in varDrugReview])
        myfile = open('FinalReviews3.csv', 'a')
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
       
        for i in result:
            print str(i)
            wr.writerow(i)
