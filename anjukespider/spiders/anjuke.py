# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from ..items import AnjukespiderItem

class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    # allowed_domains = ['anjuke.com']
    start_urls = ['https://zhengzhou.anjuke.com/sale']

    def parse(self, response):
        # 验证码处理
        # pass
        # 下一页的连接
        # next_url = response.xpath('//*[@id="content"]/div[4]/div[7]/a[7]')
        next_url = response.xpath('//*[@id="content"]/div[4]/div[7]/a[7]/@href').extract()[0]
        print("当前是" + str(next_url) + "页")
        if next_url:
            yield scrapy.Request(url = next_url ,callback=self.parse)

        # 爬取每一页所有的房屋连接
        num = len(response.xpath('//*[@id="houselist-mod-new"]/li').extract())
        print("本页一共有%s条数据"%num)
        for i in range(1,num + 1):
            url = response.xpath('//*[@id="houselist-mod-new"]/li[{}]/div[2]/div[1]/a/@href'.format(i)).extract()[0]
            print("#########################",url)
            yield scrapy.Request(url,callback=self.parse_detail)


        # 这个回调函数中使用itemloadder解析items住房信息，并返回载有信息的item

    def parse_detail(self, response):
        # houseinfo = response.xpath('//*[@class="houseInfo-wrap"]')
        # if houseinfo:
        #     print("$$$$$$$$$$$$$$$$$$$$$",response.url)
        #     l = ItemLoader(AnjukespiderItem(), houseinfo)
        #
        #
        #     l.add_xpath('mode', '//div/div[2]/dl[1]/dd/text()') # 户型
        #     print("//*[@id="content"]/div[3]/div[1]/div[3]/div/div[1]/ul/li[2]/div[1]")
        #
        #
        #     l.add_xpath('area', '//div/div[2]/dl[2]/dd/text()') # 面积
        #     l.add_xpath('floor', '//div/div[2]/dl[4]/dd/text()')# 那一层
        #     l.add_xpath('age', '//div/div[1]/dl[3]/dd/text()') # 建造年限
        #     l.add_xpath('price', '//div/div[3]/dl[2]/dd/text()')# 单价
        #     l.add_xpath('location', '//div/div[1]/dl[1]/dd/a/text()')# 位置
        #     l.add_xpath('district', '//div/div[1]/dl[2]/dd/p/a[1]/text()') # 区域
        #
        #     yield l.load_item()

        location = response.xpath("//*[@id='content']/div[4]/div[1]/div[3]/div/div/ul/li[1]/div[2]/a[1]/text()").extract_first().strip() #所属小区
        mode = response.xpath("//*[@id='content']/div[4]/div[1]/div[3]/div/div/ul/li[2]/div[2]/text()").extract_first().strip() # 户型
        price = response.xpath("//*[@id='content']/div[4]/div[1]/div[3]/div/div/ul/li[3]/div[2]/text()").extract_first().strip() #价格

        district = response.xpath("//*[@id='content']/div[4]/div[1]/div[3]/div/div/ul/li[4]/div[2]/p/a[1]/text()").extract_first().strip() #区域

        area = response.xpath("//*[@id='content']/div[4]/div[1]/div[3]/div/div/ul/li[5]/div[2]/text()").extract_first().strip() # 面积
        age = response.xpath("//*[@id='content']/div[4]/div[1]/div[3]/div/div/ul/li[7]/div[2]/text()").extract_first().strip() #建造年代
        floor = response.xpath("//*[@id='content']/div[4]/div[1]/div[3]/div/div/ul/li[11]/div[2]/text()").extract_first().strip() #所在楼层

        item = AnjukespiderItem() #实例化存储对象
        item['location'] = location
        item['mode'] = mode
        item['price'] = price
        item['district'] = district
        item['area'] = area
        item['age'] = age
        item['floor'] = floor

        print("------------------", location)
        print("------------------", mode)
        print("------------------", price)
        print("------------------", district)
        print("------------------",area)
        print("------------------",age)

        print("------------------",floor)

        yield item
    # def getHouseInfo(link):
    #     r = requests.get(link, headers=headers)
    #
    #     soup = BeautifulSoup(r.text, 'lxml')
    #
    #     house_list = soup.find_all('li', class_='list-item')
    #     # print(house_list,"+++++++++++++++++++++++++++")
    #     for house in house_list:
    #         name = house.find('div', class_='house-title').a.text.strip()
    #         price = house.find('span', class_='price-det').text.strip()
    #         price_area = house.find('span', class_='unit-price').text.strip()  # 单位面积
    #         no_room = house.find('div', class_='details-item').span.text  # 几室几厅
    #         area = house.find('div', class_='details-item').contents[3].text
    #         floor = house.find('div', class_='details-item').contents[5].text
    #         year = house.find('div', class_='details-item').contents[7].text
    #
    #         broker = house.find('span', class_='brokername').text
    #         broker = broker[1:]
    #
    #         address = house.find('span', class_='comm-address').text.strip()
    #         address = address.replace('\xa0\xa0\n', ' ')
    #
    #         tag_list = house.find_all('span', class_='item-tags')
    #         tags = [i.text for i in tag_list]
    #
    #         print(name, price, price_area, no_room, area, floor, year, broker, address, tags)