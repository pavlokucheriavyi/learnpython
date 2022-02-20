from .models import Ask, Job, Story
import requests                           # import for HTTP requests
import json                               # import to work with json objects
import re                                 # import to work with regular expressions
from base.celery import celery_app


class MyClass(object):
    """
       A class for parsing user article categories
       ...
       Atributes
       ----------
       keys_ask : list with keys of 'Ask' table in data base
       keys_job : list with keys of 'Job' table in data base
       keys_story : list with keys of 'Story' table in data base
       category : result of post request
       url : str
           link to get the id of the articles
    """
    def __init__(self, category):
        self.keys_ask = ['by', 'descendants', 'id', 'kids', 'score', 'text', 'time', 'title', 'type']
        self.keys_job = ['by', 'id', 'score', 'time', 'title', 'type', 'url']
        self.keys_story = ['by', 'descendants', 'id', 'kids', 'score', 'text', 'time', 'title', 'url']
        self.category = category
        self.url = f'https://hacker-news.firebaseio.com/v0/{self.category}.json?print=pretty'

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
        if self.category == 'askstories':
            posts = Ask.objects.all()
        elif self.category == 'jobstories':
            posts = Job.objects.all()
        else:
            posts = Story.objects.all()
        list_check_id = [i.id_articles for i in posts]

        for id_story in main_list:
            if id_story not in list_check_id:
                data_of_request = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id_story}.json?print=pretty')
                get_data_story = json.loads(data_of_request.text)

                result_list.append(get_data_story)

        return result_list

    def write_to_db(self):
        """
        The function for writing our data to data base
        """
        result_of_function = self.format_data()

        if self.category == 'askstories':
            for item in result_of_function:
                p = Ask(
                    by=item['by'],
                    descendants=item['descendants'],
                    id_articles=item['id'],
                    kids=item['kids'],
                    score=item['score'],
                    text=item['text'],
                    time=item['time'],
                    title=item['title'],
                    type=item['type']
                )
                p.save()

        elif self.category == 'jobstories':
            for item in result_of_function:
                p = Job(
                    by=item['by'],
                    id_articles=item['id'],
                    score=item['score'],
                    time=item['time'],
                    title=item['title'],
                    type=item['type'],
                    url=item['url']
                )
                p.save()
        else:
            for item in result_of_function:
                p = Story(
                    by=item['by'],
                    descendants=item['descendants'],
                    id_articles=item['id'],
                    kids=item['kids'],
                    score=item['score'],
                    text=item['text'],
                    time=item['time'],
                    title=item['title'],
                    type=item['type'],
                    url=item['url']
                )
                p.save()

    def format_data(self):
        """
        The function for formatting our json objects as needed.

        :return: the final list with json objects that store the data

        """
        stories_list = self.parse_stories()
        if len(stories_list) == 0:
            return stories_list
        else:
            if self.category == 'askstories':
                empty_keys = self.keys_ask
            elif self.category == 'jobstories':
                empty_keys = self.keys_job
            else:
                empty_keys = self.keys_story

            # if there is no desired key and value, set an empty field
            for dictionary in stories_list:
                for key in empty_keys:
                    if key not in dictionary:
                        dictionary[key] = ' '

            # to replace unreadable elements from the text:
            for dictionary in stories_list:
                for key in empty_keys:
                    if key == 'text':
                        dictionary[key] = re.sub('<[^>]*>', '', dictionary[key])
                        dictionary[key] = re.sub("&#x2F;", "/", dictionary[key])
                        dictionary[key] = re.sub("&#x27;", "'", dictionary[key])

                    elif key == 'kids':
                        dictionary[key] = list(map(str, dictionary[key]))
                        dictionary[key] = ', '.join(dictionary[key])

            return stories_list


@celery_app.task(name='article.archive_articles', queue='article')
def more(category):
    obj_1 = MyClass(category)
    obj_1.write_to_db()
