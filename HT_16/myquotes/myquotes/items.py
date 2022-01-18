# -*- coding: utf-8 -*-

import scrapy                                             # import library scrapy for parsing


class InfoItem(scrapy.Item):
    """
    А class to define the fields of our scraper, to save to a CSV file.
    Inherited from the scrapy.Item class.

    ...

    Atributes
    ---------
    title : scrapy.item.Field
        initialize 'title' field
    text : scrapy.item.Field
        initialize 'text' field
    tegs : scrapy.item.Field
        initialize 'tegs' field
    url : scrapy.item.Field
        initialize 'url' field
    """
    date = scrapy.Field()
    title = scrapy.Field()
    text = scrapy.Field()
    tegs = scrapy.Field()
    url = scrapy.Field()

# print(help(InfoItem()))                    # uncomment to review the documentation


