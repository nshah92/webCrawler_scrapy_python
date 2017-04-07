from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field

import string
import MySQLdb
import time
import csv
''' Store all a-z links to log.text 
    
    i wrote this spider for get the all links of condition from the drugs.com
'''
# class MySpider(BaseSpider):
#     name = "MyScrapper"
#     allowed_domains = ["http://drugs.com/"]
#     start_urls = []
#     start = []

    
#     for i in range(0,26):
#         start_urls.append("http://www.drugs.com/condition/"+string.lowercase[i]+".html")
#     #print start

#     def parse(self,response):
#         f = open('log1.txt','a')
#         hxs = HtmlXPathSelector(response)
#         varname=(hxs.xpath('//div[@class="contentBox"]/ul[@class="column-list-2"]/li//a/text()').extract())
#         varlink=(hxs.xpath('//div[@class="contentBox"]/ul[@class="column-list-2"]/li//a/@href').extract())
#         #print "INSERT INTO medication_details VALUES (%s, %s)" + "(varname,varlink)"

#         mydb = MySQLdb.connect(host='localhost',
#         user='root',
#         passwd='welcome',
#         db='drugs_review_drugs.com')
#         cursor = mydb.cursor()

#         for i in range(len(varname)):
#             cursor.execute("INSERT INTO medication_details(med_name, med_link) VALUES (%s, %s)", (varname[i],varlink[i]))
#             print varname[i] + varlink[i]
#             mydb.commit()
#         # print varname
#         #f.write(str(varname))
#     #mydb.commit()
#     #cursor.close()
#     #print start_urls

'''Fetch Drugs Data Review Link for each medication
    
    i wrote this spider for get the all review link from each drugs conditions link

'''
# class MySpider(BaseSpider):
#     mydb = MySQLdb.connect(host='localhost',
#     user='root',
#     passwd='welcome',
#     db='drugs_review_drugs.com')
#     cursor = mydb.cursor()

#     cursor.execute("select med_link from medication_details LIMIT 500")

#     name = "MyScrapper"
#     allowed_domains = ["http://drugs.com/"]
#     start_urls=[]

#     for i in cursor:
#         link=str(i).replace("(","").replace(")","").replace(",","").replace("'","")
#         start_urls.append("http://www.drugs.com"+link+"?sort=drug&order=asc")
#     # #print start_urls
#     # start_urls=["http://www.drugs.com/condition/acne.html?sort=drug&order=asc"]

#     def parse(self,response):
#         f = open('logReviewLink.txt','a')
#         hxs = HtmlXPathSelector(response)
#         varDrugReview = (hxs.xpath('//div[@id="conditionBoxWrap"]/table[@id="conditionbox"]/tr/td[@class="nowrap review-count"]/a/text()').extract())
#         varDrugReviewLink = (hxs.xpath('//div[@id="conditionBoxWrap"]/table[@id="conditionbox"]/tr/td[@class="nowrap review-count"]/a/@href').extract())        

#         print len(varDrugReview)
#         print len(varDrugReviewLink)
#         #f.write(str(varDrugReviewLink))
#         # med_id=[]
           
#         mydb = MySQLdb.connect(host='localhost',
#         user='root',
#         passwd='welcome',
#         db='drugs_review_drugs.com')
#         cursor1 = mydb.cursor()

#         # cursor.execute("select med_ID from medication_details")
#         # for i in cursor:
#         #     # print str(i).replace("(","").replace(")","").replace(",","").replace("'","").replace("L","")
#         #     med_id.append(str(i).replace("(","").replace(")","").replace(",","").replace("'","").replace("L",""))

#         for i in range(len(varDrugReview)):
#             cursor1.execute("INSERT INTO review_demo(noofreview,link) VALUES (\'{0}\',\'{1}\')".format(varDrugReview[i],varDrugReviewLink[i]))
#             mydb.commit()
#         cursor1.close()

#         # for link,num in varDrugReviewLink,varDrugReview:
#         #     # print "INSERT INTO drugs_details(review_link) VALUES (\'{0}\')".format(link)
#         #     cursor1.execute("INSERT INTO review_demo(noofreview,review_link) VALUES (\'{0}\',\'{1}\')".format(num,link))
#         #     mydb.commit()
#         # cursor1.close()
'''Fetchin review data from each link

    By this spider we can get the review from each link we generated previous
'''

class MySpider(BaseSpider):
    name = "MyScrapper"
    allowed_domains = ["http://drugs.com/"]
    
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='welcome',
    db='drugs_review_drugs.com')
    cursor = mydb.cursor()

    cursor.execute("select distinct link from review_demo where noofreview not like '0%' LIMIT 100 OFFSET 1066")
    
    a='http://www.drugs.com/comments/isotretinoin/absorica-for-acne.html'
    start_urls=[]
    for i in cursor:
        link=str(i).replace("(","").replace(")","").replace(",","").replace("'","")
        for i in range(1,20):
            start_urls.append("http://www.drugs.com"+link+"?page="+str(i))
        print start_urls
    def parse(self,response):
        f = open('Demo.csv','a')
        hxs = HtmlXPathSelector(response)
        varReviewID = (hxs.xpath('//div[@class="contentBox"]/div/div/div[@class="user-comment"]/p[@class="user-name user-type user-type-2_non_member"]/text()').extract())
        varReview = (hxs.xpath('//div[@class="contentBox"]/div/div/div[@class="user-comment"]//p[1]//span//text()').extract())
        print [x.encode('ascii', 'ignore') for x in varReview]
        print varReviewID   
        
        mydb = MySQLdb.connect(host='localhost',
        user='root',
        passwd='welcome',
        db='drugs_review_drugs.com')
        cursor1 = mydb.cursor()
        name=list()
        for j in range(len(varReview)):
            name.append("drugs.com")
        result = zip(name,varReviewID,[x.encode('ascii', 'ignore') for x in varReview])
        myfile = open('finalDrugReview.csv', 'a')
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for row in result:
            wr.writerow(row)