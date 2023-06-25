import scrapy

from scrspyDemo.items import ScrspydemoItem


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["netflav.com"]
    start_urls = ["https://netflav.com/chinese-sub"]

    def parse(self, response):
        '''
        当下载器把URL 对应的响应交给引擎后 引擎就调用爬虫该方法
        用于处理响应的  1。 解析提取数据 2.提取新的URL
        :param response:  URL对应的响应数据
        :return:
        '''
        # 包二进制数据写入到文件中
        # with open('teacher.html','wb') as f:
        #     f.write(response.body)
        '''
        <li>
        <div class="teamain">
        <div class="main_pic">
        <img src="/images/teacher/20211531171513782.jpg" class="mCS_img_loaded">
        </div>
        <div class="main_bot">
        <h2 xt-marked="ok">杨老师<span xt-marked="ok">课程研究员</span></h2>
        <h3><span xt-marked="ok">北大方正</span><span xt-marked="ok"> 12年经验</span></h3>
        <p xt-marked="ok">研发成果：<span xt-marked="ok">Redis</span><span xt-marked="ok"> RabbitMQ</span></p>
        </div><div class="main_mask">
        <h2>杨老师<span>课程研究员</span></h2>
        <h3>入职时间：2018-10-01</h3>
        <p>10年以上IT相关经验，曾在北大方正担任项目经理。2010年起转架构，在互联网，游戏公司担任技术经理职务。精通Spring相关开发框架，在项目中熟练运用缓存技术和消息中间技术，对分布式及微服务架构有深入理解。	</p></div></div><div class="teamain"><div class="main_pic"><img src="/images/teacher/20231817161820244.jpg" class="mCS_img_loaded"></div><div class="main_bot"><h2 xt-marked="ok">苏老师<span xt-marked="ok">课程研究员</span></h2><h3><span xt-marked="ok">Vue</span><span xt-marked="ok"> TypeScript</span><span> 小程序</span></h3><p xt-marked="ok">研发成果：<span xt-marked="ok">小兔鲜儿小程序项目</span><span xt-marked="ok">小兔鲜儿Vue3+TS项目</span></p></div><div class="main_mask"><h2>苏老师<span>课程研究员</span></h2><h3>入职时间：2015-12-01</h3><p>6年+从业经验，精通HTML5, CSS3, JavaSript,熟悉Vue, React, Angular,jQuery, BootStrap。特别擅长微信小程序，首次研发和实施了完整的微信小程序商城项目。教学细腻，能够深入浅出地剖析知识点。						</p>
        </div>
        </div>
        </li>
        '''

        #  xpath  提取数据
        divs = response.xpath('//div[@class="grid_title"]')
        print(len(divs))
        # print(divs)
        # 遍历获取想要的数据
        for div in divs:
            item = ScrspydemoItem()
            # item['name'] =div.xpath('./h2/text()').extract()[0]
            # item['title'] =div.xpath('./span/text()').extract()[0]
            # item['desc'] =div.xpath('./h3/text()').extract()[0]

            item['name'] = div.xpath('./h2/text()').extract_first()
            item['title'] = div.xpath('./span/text()').extract_first()
            item['desc'] = div.xpath('./h3/text()').extract_first()
            # print(item)

            # yield item





        pass


