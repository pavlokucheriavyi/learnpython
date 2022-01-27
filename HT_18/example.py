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

            result_list.append(get_data_story)

        return result_list

    def write_csv(self):
        """
        The function for writing our data to a csv file
        """
        with open('result.csv', 'w') as file:
            file_writer = csv.writer(file, delimiter='*')

            result_of_function = self.format_data()
            final_list_to_csv = result_of_function[0]
            final_list_keys = result_of_function[1]

            file_writer.writerow(final_list_keys)
            for item in final_list_to_csv:
                # collect the data in the dictionary in order for correct writing to the csv file
                values_list = []
                for key in final_list_keys:
                    values_list.append(item[key])
                file_writer.writerow(values_list)


    def format_data(self):
        """
        The function for formatting our json objects as needed.
        The function also defines the maximum number of fields
        of our articles to be written to the csv file

        :return: 1) the final list with json objects that store the data
                 2) all possible keys to write to the csv file

        """
        stories_list = self.parse_stories()
        max_len = 0
        result_list_keys = None

        # define the maximum possible number of fields to write to the csv file
        for dictionary in stories_list:
            if len(dictionary) > max_len:
                max_len = len(dictionary)

        for dictionary in stories_list:
            if len(dictionary) == max_len:
                result_list_keys = list(dictionary.keys())
                break

        # if there is no desired key and value, set an empty field
        for dictionary in stories_list:
            for key in result_list_keys:
                if key not in dictionary:
                    dictionary[key] = ' '

        # to replace unreadable elements from the text:
        for dictionary in stories_list:
            for key in result_list_keys:
                if key == 'text':
                    dictionary[key] = re.sub('<[^>]*>', '', dictionary[key])
                    dictionary[key] = re.sub("&#x2F;", "/", dictionary[key])
                    dictionary[key] = re.sub("&#x27;", "'", dictionary[key])

                elif key == 'kids':
                    dictionary[key] = list(map(str, dictionary[key]))
                    dictionary[key] = ', '.join(dictionary[key])

        return stories_list, result_list_keys


obj_1 = MyClass()
obj_1.write_csv()
