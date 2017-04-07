from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field
from scrapy.cmdline import execute

import string
import MySQLdb
import time
import csv
import itertools

'''
    Getting all link Drugs & Medication A-z
    below code is for retrive link for review one Medication

    PART 1
'''

class MySpider(BaseSpider):
    name = "MyScrapperWebMD"
    allowed_domains = ["http://webmd.com/"]
    
    start_urls=["http://www.webmd.com/drugs/index-drugs.aspx?alpha=0&subTab=0&show=drugs"]
    for i in range(0,26):
        for j in range(1,5):
            start_urls.append("http://www.webmd.com/drugs/index-drugs.aspx?alpha="+string.lowercase[i]+"&subTab="+str(j)+"&show=drugs")
    # print start_urls
    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        varlink1 = (hxs.xpath('//div[@id="drugs-az-list"]/div[@id="az-box"]/div[@class="az-content"]/ul[@class="az-col-left"]/li[@class="odd_row_fmt"]/p/a/@href').extract())
        
        print varlink1
        result = zip([x.encode('ascii', 'ignore') for x in varlink1])
        myfile = open('link1.csv', 'a')
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for row in result:
            wr.writerow(row)
'''
    PART 2
    filtering the above link (Checking whether reviews are exist or not)

    After executing this you have only those link which medication have reviews...
'''

# class MySpider(BaseSpider):
#     name = "MyScrapperWebMD"
#     allowed_domains = ["http://webmd.com/"]
#     start_urls=["http://www.webmd.com/drugs/2/drug-64439/abilify-oral/details"]

#     myfile=open('link1.csv')
#     for row in myfile:
#         start_urls.append("http://www.webmd.com"+str(row).replace("\r", "").replace("\n", "").replace('"',""))
#     # print start_urls
#     def parse(self,response):
#         hxs=HtmlXPathSelector(response)
#         varBubble=(hxs.xpath('//div[@class="monograph-navigation"]/nav[@class="monograph-menu"]/ul[@class="tabs"]/li[@class="reviews"]/span[@class="bubble"]/text()').extract())
#         print varBubble
#         if(varBubble!=[]):
#             varlink1=(hxs.xpath('//div[@class="monograph-navigation"]/nav[@class="monograph-menu"]/ul[@class="tabs"]/li[@class="reviews"]/a/@href').extract())
#             print varlink1
#             result = zip([x.encode('ascii', 'ignore') for x in varlink1])
#             myfile = open('link2.csv', 'a')
#             wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#             for row in result:
#                 wr.writerow(row)

'''
    PART 3

    Finally extract the all review for each medication

    get Review and drugname
'''

# class MySpider(BaseSpider):
#     name = "MyScrapperWebMD"
#     allowed_domains = ["http://webmd.com/"]
#     start_urls=[]
#     myfile=open('link2.csv')
#     drug=""
#     for row in myfile:
#         for i in range(1,100):
#             start_urls.append("http://www.webmd.com"+row.replace("\r", "").replace("\n", "").replace('"',"")+"&pageIndex="+str(i)+"&sortby=3&conditionFilter=-1")
#     def parse(self,response):
#         hxs = HtmlXPathSelector(response)
#         varDrugname=(hxs.xpath('//div[@id="mainContent_ThirdCol_ctr"]/div[@id="ContentPane4"]/div[@id="header"]/div[@class="tb_main"]/h1/text()').extract())
#         varReviewID = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@class="reviewerInfo"]/text()').extract())
#         varReview1 = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull1"]/text()').extract())
#         varReview2= (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull2"]/text()').extract())
#         varReview3 = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull3"]/text()').extract())
#         varReview4 = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull4"]/text()').extract())
#         varReview5 = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull5"]/text()').extract())

#         varReview= [x.encode('ascii', 'ignore') for x in varReview1]+[x.encode('ascii', 'ignore') for x in varReview2]+[x.encode('ascii', 'ignore') for x in varReview3]+[x.encode('ascii', 'ignore') for x in varReview4]+[x.encode('ascii', 'ignore') for x in varReview5]
#         drug=varDrugname[0].replace("User Reviews & Ratings - ","")
#         name=list()
#         for j in range(len(varReview)):
#             name.append("webmd.com")
#         for k in range(len(varReview)-1):
#             varDrugname.append(drug)
#         result=zip(name,varReviewID,varDrugname,varReview)
#         myfile = open('finalDrugReview1.csv', 'a')
#         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#         for row in result:
#             wr.writerow(row)