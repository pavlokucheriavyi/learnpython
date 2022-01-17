from urllib.parse import urljoin                               # import 'urljoin' for url's concatenation
import scrapy                                                  # import library scrapy for parsing
from bs4 import BeautifulSoup                                  # import library BeautifulSoup for parsing

from myquotes.enter_function import var_for_spider             # import the variable to determine the date of the news to be parsed
from myquotes.items import InfoItem                            # import class InfoItem for initialize the scraper fields


class MySpider(scrapy.Spider):
    """
       А class parses the city news for the specified date and
       passes the spyder to other imported files of the project
       to save to a csv file

       ...

       Atributes
       ---------
       name : str
          the name of our spyder
       allowed_domains : list
          the list contains one value of str type - the domain
          specified when the scrapy project was created
       start_urls : list
          the list contains one value of str type - the base url
          of the site we are going to parse
       URL : str
          the base url of the site we are going to parse, created
          to concatenate with the date of the myquotes to be parsed
    """

    name = 'mainspider'
    allowed_domains = ['vikka.ua']
    start_urls = ['http://vikka.ua/']
    URL = 'https://www.vikka.ua/'

    def start_requests(self):
        """
        The function creates a main page for parsing and
        passes it to the parse_page function, to do work on
        that page (using the yield method).
        """

        parse_page = urljoin(self.URL, var_for_spider)
        yield scrapy.Request(
            url=parse_page,
            callback=self.parse_page
        )

    def parse_page(self, response):
        """
        The function parses the main news page for a given date,
        determines url to each news page by calling the function
        'parse_news', and passes it to the 'more_info'
        function (using the yield method), to do work on that page.

        :param response: url of main page for parsing
        """
        soup = BeautifulSoup(response.text, 'lxml')
        for item in soup.select('div.col-sm-8'):
            main_dict = self.parse_news(item)
            link = main_dict['url']
            yield scrapy.Request(
                url=link,
                callback=self.more_info
            )
        # find the next news page, and pass url of this page
        # to the 'parse_page' function for parsing using yield method.
        # If there is no page, then terminate the function.
        next_page = soup.select_one('a.next.page-numbers')
        if not next_page:
            return
        next_url = next_page.get('href')
        yield scrapy.Request(
            url=next_url,
            callback=self.parse_page
        )


    def parse_news(self, soup):
        """
        The function that returns a dictionary with the 'url' key
        and the value - a url to a particular news item.

        :param soup: a block with a particular news item for parsing
        :return: dictionary with value - a url, to a particular news item
        """
        return {
            'url': soup.select_one('h2.title-cat-post > a').get('href')
        }


    def more_info(self, response):
        """
        1) The function that parses a particular news page and initializes a
        dictionary with the necessary data by calling the
        function 'more_info_data'. 2) Completes this dictionary with a link
        to the news. 3) Returns, using the yield method, the InfoItem class
        by passing in the final dictionary to save in a csv file.

        :param response: url of a particular news item to be parsed
        """
        soup = BeautifulSoup(response.text, 'lxml')
        my_dict = self.more_info_data(soup)
        # we take from the response url parameter, using the 'response.url' command
        my_dict['url'] = response.url

        yield InfoItem(**my_dict)

    def more_info_data(self, soup):
        """
        The function returns a dictionary with the necessary data about the news.
        Gets formatted tags using the get_tegs function,
        passing in all the tags of the news.

        :param soup: a page with a particular news item for parsing
        :return: dictionary with the necessary data about the news
        """
        return {
            'title': soup.select_one('h1.post-title').text,
            'text': soup.select_one('div.entry-content.-margin-b').text,
            'tegs': self.get_tegs(soup.select('a.post-tag'))
        }

    def get_tegs(self, main_list):
        """
        The function returns formatted news tags in the format 'str'.

        :param main_list: a list of unformatted tags
        :return: formatted news tags in the format 'str'
        """
        midlle_list = []
        for item in main_list:
            midlle_list.append('#' + item.text.capitalize())
        result_string = ', '.join(midlle_list)
        return result_string

# print(help(MySpider()))                       # uncomment to review the documentation

