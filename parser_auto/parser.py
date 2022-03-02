import requests
from bs4 import BeautifulSoup
import json

def reverse_dict(dict_main):
    final_dict = {}

    # переворачиваем екстенд дикт
    x = list(dict_main.items())

    for k, v in reversed(x):
        final_dict[k] = v

    # и расширяем его с начальным диктом
    return final_dict



def get_first_news():
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'

    }

    url = "https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&brand.id[0]=15&country.import.usa.not=-1&price.USD.lte=8000&price.currency=1&sort[0].order=dates.created.desc&abroad.not=0&custom.not=1&page=0&size=20"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    news = soup.select('div.content-bar')
    new_dict = {}
    end_dict = {}

    for item in news:
        title = item.select_one('a.address').text.strip()
        link = item.select_one('a.address').get('href')
        price = item.select_one('span.bold.green.size22').text
        time = item.select_one('div.footer_ticket').text.strip()

        list1 = link.split('_')
        end = list1[-1][:-5:]

        new_dict[end] = {
            'title': title,
            'link': link,
            'price': price,
            'time': time
        }

    end_dict = reverse_dict(new_dict)

    with open("news_dict.json", "w") as file:
        json.dump(end_dict, file, indent=4, ensure_ascii=False)


def check_news_update():
    with open("news_dict.json") as file:
        news_dict = json.load(file)

    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Mobile Safari/537.36'
    }

    url = "https://auto.ria.com/uk/search/?indexName=auto,order_auto,newauto_search&categories.main.id=1&brand.id[0]=15&country.import.usa.not=-1&price.USD.lte=8000&price.currency=1&sort[0].order=dates.created.desc&abroad.not=0&custom.not=1&page=0&size=20"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    news = soup.select('div.content-bar')

    fresh_news = {}
    extend_dict = {}

    for item in news:
        link = item.select_one('a.address').get('href')
        list1 = link.split('_')
        end = list1[-1][:-5:]

        if end in news_dict:
            continue
        else:
            title = item.select_one('a.address').text.strip()
            link = item.select_one('a.address').get('href')
            price = item.select_one('span.bold.green.size22').text
            time = item.select_one('div.footer_ticket').text.strip()

            list1 = link.split('_')
            end = list1[-1][:-5:]

            extend_dict[end] = {
                'title': title,
                'link': link,
                'price': price,
                'time': time
            }

            fresh_news[end] = {
                'title': title,
                'link': link,
                'price': price,
                'time': time
            }

    x = reverse_dict(extend_dict)
    news_dict.update(x)

    fresh_news = reverse_dict(fresh_news)

    with open("news_dict.json", "w") as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return fresh_news


def main():
    # get_first_news()
    print(check_news_update())


if __name__ == '__main__':
    main()
