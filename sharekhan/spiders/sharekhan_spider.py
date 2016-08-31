import scrapy
import unicodedata

from scrapy.loader import ItemLoader
from sharekhan.items import SharekhanItem

class ShareKhanSpider(scrapy.Spider):
    name = "sharekhan"
    allowed_domains = ["moneycontrol.com"]
    start_urls = [
        "http://www.moneycontrol.com/financials/bayercropscience/profit-loss/BC12"
   ]

    def parse(self, response):

        #l=ItemLoader(item=SharekhanItem(), response=response)

        r1=(response.xpath('//table[@class="table4"]/tr[18]/td[2]/text()').extract())
        r1e=(response.xpath('//table[@class="table4"]/tr[36]/td[2]/text()').extract())

        r1s=str(r1[0])
        r1es=str(r1e[0])

        r2=(response.xpath('//table[@class="table4"]/tr[18]/td[3]/text()').extract())
        r2e=(response.xpath('//table[@class="table4"]/tr[36]/td[3]/text()').extract())

        r2s=str(r2[0])
        r2es=str(r2e[0])


        r3=(response.xpath('//table[@class="table4"]/tr[18]/td[4]/text()').extract())
        r3e=(response.xpath('//table[@class="table4"]/tr[36]/td[4]/text()').extract())

        r3s=str(r3[0])
        r3es=str(r3e[0])


        r4=(response.xpath('//table[@class="table4"]/tr[18]/td[5]/text()').extract())
        r4e=(response.xpath('//table[@class="table4"]/tr[36]/td[5]/text()').extract())

        r4s=str(r4[0])
        r4es=str(r4e[0])


        r5=(response.xpath('//table[@class="table4"]/tr[18]/td[6]/text()').extract())
        r5e=(response.xpath('//table[@class="table4"]/tr[36]/td[6]/text()').extract())

        r5s=str(r5[0])
        r5es=str(r5e[0])


        
         
        filename = response.url.split("/")[-3] + '.eps'
        with open(filename, 'wb') as f:
            f.write(r1s+"\t"+r1es+"\n")
            f.write(r2s+"\t"+r2es+"\n")
            f.write(r3s+"\t"+r3es+"\n")
            f.write(r4s+"\t"+r4es+"\n")
            f.write(r5s+"\t"+r5es+"\n")
            f.close()

              

        
         



        
        
        # filename = response.url.split("/")[-3] + '.eps'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
