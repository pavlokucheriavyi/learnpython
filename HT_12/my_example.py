import lxml
from bs4 import BeautifulSoup as bs
import requests
import csv
from datetime import datetime


start_time = datetime.now()

result = []

def about_author(author_string):
    URL = 'https://quotes.toscrape.com' + author_string
    r = requests.get(URL)
    soup = bs(r.text, 'lxml')
    return_list = []

    my_var_first = soup.select_one('span.author-born-date').get_text() + ' ' + soup.select_one('span.author-born-location').get_text()
    my_var_second = soup.select_one('.author-description').get_text().strip()

    return_list.append(my_var_first)
    return_list.append(my_var_second)

    return return_list



def main(link=''):
    result_list = []

    URL = 'https://quotes.toscrape.com'
    r = requests.get(URL + link)
    soup = bs(r.text, 'lxml')

    list_main = soup.select('.quote')

    for item in list_main:
        something = item.select_one('div.quote span a[href]').get('href')
        my_list = about_author(something)
        result_list.append(
            {'text' : item.select_one('span.text').get_text(),
             'author' : item.select_one('small.author').get_text(),
             'born' : my_list[0],
             'description' : my_list[1]
            }
        )

    return result_list


def write_csv(main_list):
    with open('result.csv', 'w') as file:
        file_writer = csv.writer(file, delimiter='*')
        file_writer.writerow(['Text:', 'Author:', 'Born:', 'Description:'])
        for item in main_list:
            file_writer.writerow([item['text'], item['author'], item['born'], item['description']])



def get_links():
    main_list = []
    main_link = ''

    flag = True
    while flag == True:
        URL = 'https://quotes.toscrape.com'
        r = requests.get(URL + main_link)
        soup = bs(r.text, 'lxml')

        check_link = soup.select_one('li.next a[href]')

        main_list.append(check_link)

        if main_list[-1] == None:
            return main_list

        new_link = soup.select_one('li.next a[href]').get('href')
        main_link = new_link

links_list = get_links()
start_list = main()


for i in links_list:
    if i == None:
        break
    ex_list = main(i.get('href'))
    start_list.extend(ex_list)


write_csv(start_list)

print(datetime.now() - start_time)
















