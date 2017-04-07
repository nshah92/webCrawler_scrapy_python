from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field
from scrapy.cmdline import execute

import string
import time
import csv
import itertools

class MySpider(BaseSpider):
    name = "ReviewBuilder"
    allowed_domains = ["https://drugs.com/"]
    start_urls = []
    for i in range(1,20):
        start_urls.append("https://www.drugs.com/comments/losartan/"+"?page="+str(i))
    def parse(self,response):
        hxs = HtmlXPathSelector(response)
        varDrugName = (hxs.xpath('//div[@class="contentBox"]/h1/text()')).extract()
        varDrugReview = (hxs.xpath('//div[@class="user-comment"]/p[1]/span//text()')).extract()
        varDrugDate = (hxs.xpath('//div[@class="user-comment"]/p[@class="user-name user-type user-type-2_non_member"]/span[@class="light comment-date"]/text()')).extract()
    
        DrugName = [x.encode('ascii', 'ignore') for x in varDrugName]

        name = list()
        genericname = list()

        time.sleep(5)
        for j in range(len(varDrugReview)):
            name.append(DrugName[0].replace("User Reviews for","").replace("[","").replace("]","").replace("'","").strip())
        for j in range(len(varDrugReview)):
            genericname.append("Cozaar")
        result = zip(name, genericname,[x.encode('ascii', 'ignore') for x in varDrugReview], varDrugDate)
        myfile = open('finalDrugReview_with_dates1.csv', 'a')
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for i in result:
            print str(i)
            wr.writerow(i)

# class MySpider(BaseSpider):
#     name = "ReviewBuilder"
#     allowed_domains = ["http://webmd.com/"]
#     start_urls=[]
#     drug=""
#     for i in range(1,500):
#         start_urls.append("http://www.webmd.com/drugs/drugreview-6616-losartan+oral.aspx?drugid=6616&drugname=losartan+oral"
#                             +"&pageIndex="
#                             +str(i)
#                             +"&sortby=3&conditionFilter=-1")
#     def parse(self,response):
#         hxs = HtmlXPathSelector(response)
#         varDrugname=(hxs.xpath('//div[@id="mainContent_ThirdCol_ctr"]/div[@id="ContentPane4"]/div[@id="header"]/div[@class="tb_main"]/h1/text()').extract())
#         varReviewID = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@class="reviewerInfo"]/text()').extract())
#         varReview1 = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull1"]/text()').extract())
#         varReview2= (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull2"]/text()').extract())
#         varReview3 = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull3"]/text()').extract())
#         varReview4 = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull4"]/text()').extract())
#         varReview5 = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/p[@id="comFull5"]/text()').extract())

#         varDrugDate = (hxs.xpath('//div[@id="ratings_fmt"]/div[@class="userPost"]/div[@class="postHeading clearfix"]/div[@class="date"]/text()').extract())

#         varReview= [x.encode('ascii', 'ignore') for x in varReview1]+[x.encode('ascii', 'ignore') for x in varReview2]+[x.encode('ascii', 'ignore') for x in varReview3]+[x.encode('ascii', 'ignore') for x in varReview4]+[x.encode('ascii', 'ignore') for x in varReview5]
#         drug=varDrugname[0].replace("User Reviews & Ratings - ","")
#         name=list()
#         brandname = list()

#         for j in range(len(varReview)):
#             brandname.append("Cozzar")
#         for k in range(len(varReview)-1):
#             varDrugname.append(drug)
#         result=zip(varDrugname,brandname,varReview, varDrugDate)
#         myfile = open('finalDrugReview_with_dates1.csv', 'a')
#         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#         for row in result:
#             print row
#             wr.writerow(row)