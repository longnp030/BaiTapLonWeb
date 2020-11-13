from os import scandir
import scrapy


class Course(scrapy.Item):
    name = scrapy.Field()
    publishdate = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()


class EDX(scrapy.Spider):
    name = 'edx'

    start_urls = ['https://www.classcentral.com/provider/coursera', ]
    base_url = 'https://www.classcentral.com/provider/coursera'
    root_url = 'https://www.classcentral.com'

    def parse(self, response):
        MAX_PAGE_SIZE = 1
        for page_count in range(1, MAX_PAGE_SIZE + 1):
            url_with_page_count = self.base_url + '?page=' + str(page_count)
            yield scrapy.Request(url=url_with_page_count, callback=self.parse_base_url_with_page_count)
    
    def parse_base_url_with_page_count(self, response):
        courses_count_on_this_page = len(response.css('tr'))
        print(courses_count_on_this_page)
        course_links = []
        for i in range(courses_count_on_this_page + 1):
            try:
                course_link = response.css('tr')[i].css('td')[1].css('a')[1].css('a::attr(href)').extract()[0]
                if 'http' not in course_link:
                    course_links.append(course_link)
            except Exception as e:
                pass
        print(course_links)
        for course_link in course_links:
            yield scrapy.Request(url=self.root_url + course_link, callback=self.parse_course)

    def parse_course(self, response):
        course = Course()
        try:
            course['name'] = response.css('.head-1::text').get()
        except:
            course['name'] = ''
        try:
            course['publishdate'] = response.css('select')[0].css('option::text')[0].get().strip()
        except:
            course['publishdate'] = ''
        course['price'] = 0
        try:
            course['description'] = response.css('div.text-1::text').get().strip()
        except:
            course['description'] = ''

        print(course)

        f = open('../courses.txt', 'a')
        f.write(str(course)+'\n')
