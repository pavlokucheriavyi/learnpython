# -*- coding: utf-8 -*-
# Define your item pipelines here

import os                                               # import os to work with the operating system
from datetime import datetime                           # import the datetime module for date processing
from pathlib import Path                                # import Path to create a specific path
from scrapy.exporters import CsvItemExporter            # import this class to save the data in a csv file

from myquotes.items import InfoItem                     # import this class to verify correspondence of the set fields


def enter_date():
    """
    The function asks the user to enter the date
    and checks if it is correct

    :return: date entered by the client
    """
    flag = True
    while flag:
        try:
            date = input('Enter the date of the news you would like to read, '
                         'in format - day, month, year. example(5.1.2022): ')

            date_format = "%d.%m.%Y"
            start = datetime.strptime(date, date_format)
            now = datetime.now()

            if start > now:
                print('Your date in the future, please enter again')
            else:
                my_string = date.split('.')
                # the var 'res_string' initializes the date in a format
                # suitable for concatenation from the main scraper url
                res_string = "/".join(reversed(my_string)) + '/'
                # with return exits the infinite loop if the date is entered correctly
                return res_string
        except ValueError:
            print('You entered the wrong date. Please repeat again. Example(12.11.2021)')


# a variable to send the date to the scraper
var_for_spider = enter_date()
# the variable formats the result of the function 'enter_date'
# function to pass the date in the name of the future csv file
var_for_name_of_file = '_'.join(var_for_spider.split('/'))[:-1:]


class SaveToCSVPipeLine(object):
    """
    A class loads data pulled from the scraper into a csv file.
    If there is no file, it creates a new one.
    If there is a file, it overwrites it

    ...

    Atributes
    ----------
    fields_to_export : list
        a list of future rows that will be loaded into the csv file
    report_file_name : str
        a variable to initialize the csv file name
    """
    fields_to_export = []
    report_filename = ''

    def open_spider(self, spider):
        """
        function for opening the scraper

        :param spider: our scraper
        """
        self.file = None

    def close_spider(self, spider):
        """
        function for closing the scraper

        :param spider: our scraper
        """
        if self.file:
            self.file.close()

    def process_item(self, item, spider):
        """
        function overwrites our item to a csv file. If it does not exist,
        it creates a new one using the function 'init_exporter' by
        passing the file path to it.

        :param item: the final data object of our scraper in key-value format
        :param spider: our scraper
        :return: the final data object of our scraper
        """
        if not self.file:
            self.init_exporter(Path(__file__).parent.parent / 'reports')
        self.exporter.export_item(item)
        return item

    def init_exporter(self, report_path):
        """
        A function creates a new file if it does not exist
        and uploads the data from our scraper there

        :param report_path: the path where to create the file
        """
        if not os.path.isdir(report_path):
            os.makedirs(report_path)
        filename = os.path.join(report_path, f'{self.report_filename}.csv')
        self.file = open(filename, 'wb')
        self.exporter = CsvItemExporter(self.file, fields_to_export=self.fields_to_export)


class SaveToCSVPipeLineInfo(SaveToCSVPipeLine):
    """
    A class loads our data from 'mainspider.py' pulled from
    the scraper into a csv file.
    Inherited from class SaveToCSVPipeLine. The class SaveToCSVPipeLine
    has the main functionality.

    ...

    Atributes
    ---------
    fields_to_export : tuple
        keys from our scraper dictionary. Variable overwrites
        the SaveToCSVPipeLine class variable 'fields_to_export'
    report_filename : str
        name of our csv file. Variable overwrites
        the SaveToCSVPipeLine class variable 'report_filename'
    """
    fields_to_export = (
        'title',
        'text',
        'tegs',
        'url'
    )

    report_filename = var_for_name_of_file

    def my_process_item(self, item, spider):
        """
        The function checks if our final scraper
        dictionary belongs to the set class in 'items.py'.
        If yes, it passes our dictionary to other functions
        for writing to the csv file

        :param item: the final data object of our scraper in key-value format
        :param spider: our spider 'mainspider.py'
        :return: the final data object of our scraper
        """
        if isinstance(item, InfoItem):
            return self.process_item(item, spider)
        return item


# print(help(enter_date))                                  # uncomment one of these functions to see the documentation
# print(help(SaveToCSVPipeLine()))
# print(help(SaveToCSVPipeLineInfo()))