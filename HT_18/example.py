import requests                           # import for HTTP requests
import json                               # import to work with json objects
import csv                                # import for work with csv files
import re                                 # import to work with regular expressions
import sys                                # import to access some variables used or supported by the interpreter

# list of command line arguments passed to the Python script
commands_list = sys.argv


class MyClass(object):
    """
       A class for parsing user article categories
       ...
       Atributes
       ----------
       categories : list
           list of categories for parsing
       category : result of function 'enter_category()'
           category for parsing specified by the user
       url : str
           link to get the id of the articles
    """
    def __init__(self):
        self.categories = ['askstories', 'showstories', 'newstories', 'jobstories']
        self.category = self.enter_category()
        self.url = f'https://hacker-news.firebaseio.com/v0/{self.category}.json?print=pretty'



    def enter_category(self):
        """
        The function determines whether there is a category
        to be parsed and returns the category if it is specified

        :return: the category we need
        """
        if len(commands_list) != 2:
            return 'newstories'
        elif commands_list[1] in self.categories:
            return commands_list[1]
        else:
            raise TypeError('Your category does not belong on the list.')

    def parse_category_page(self):
        """
        The function to get a json object with the
        id of the articles, using a request
        :return: a json object with the articles id
        """
        page = requests.get(self.url)

        data_json = json.loads(page.text)

        return data_json

    def parse_stories(self):
        """
        The function for parsing the data of articles, of a specified
        category and collecting these articles into a final list
        :return: list with json objects of our articles
        """
        main_list = self.parse_category_page()
        result_list = []
        for id_story in main_list:
            data_of_request = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id_story}.json?print=pretty')
            get_data_story = json.loads(data_of_request.text)

            result_dict = self.format_data(get_data_story)

            result_list.append(result_dict)

        return result_list

    def write_csv(self):
        """
        The function for writing our data to a csv file
        """
        with open('result.csv', 'w') as file:
            file_writer = csv.writer(file, delimiter='*')
            result = self.parse_stories()

            file_writer.writerow(['by', 'descendants', 'id', 'kids', 'score', 'text', 'time', 'title', 'type', 'url'])
            for item in result:
                file_writer.writerow([item['by'], item['descendants'], item['id'], item['kids'], item['score'],
                                      item['text'], item['time'], item['title'], item['type'], item['url']])

    def format_data(self, my_dict):
        """
        The function for formatting our json objects as needed
        :param my_dict: a list with json objects that store the data
        :return: the final list with json objects that store the data
        """
        values_list = ['by', 'descendants', 'id', 'kids', 'score', 'text', 'time', 'title', 'type', 'url']

        for i in values_list:
            if i not in my_dict:
                my_dict[i] = ' '

        # to replace unreadable elements from the text:
        my_dict['text'] = re.sub('<[^>]*>', '', my_dict['text'])
        my_dict['text'] = re.sub("&#x2F;", "/", my_dict['text'])
        my_dict['text'] = re.sub("&#x27;", "'", my_dict['text'])

        my_dict['kids'] = list(map(str, my_dict['kids']))
        my_dict['kids'] = ', '.join(my_dict['kids'])

        return my_dict


obj_1 = MyClass()
obj_1.write_csv()
