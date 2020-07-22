import requests
from bs4 import BeautifulSoup
from traceback import print_exc


def get_news(category):

    news = {
        'success': 'True',
        'catagory': category,
        'Articles': []
    }

    if category != 'latest':
        base_url = "https://inshorts.com/en/read/" + category
    else:
        base_url = "https://inshorts.com/en/read"

    r = requests.get(base_url)

    soup = BeautifulSoup(r.text, "lxml")

    data = soup.find_all('div', {"class": "news-card"})

    for article in data:

        try:
            content = article.find('div', {'itemprop': 'articleBody'}).text
            # print(content)
        except:
            content = None

        try:
            author = article.find(class_='author').text
        except:
            author = None

        try:
            date = str(article.find(clas='date').text) + " " + \
                str(article.find(class_='time').text)
        except Exception as e:
            print_exc()
            date = None

        try:
            image_url = (article.find(
                class_='news-card-image')['style'].split("'")[1])[:-1]
        except Exception as e:
            print_exc()
            image_url = None

        try:
            title = article.find('span', {'itemprop': 'headline'}).text
        except:
            title = None

        try:
            read_more_url = article.find(class_='read-more').find('a')['href']
        except:
            read_more_url = None

        try:
            inshort_url = "https://inshorts.com" + \
                article.find(class_='news-card-title').find('a')['href']
        except:
            inshort_url = None

        data = {'author': author, 'content': content, 'date': date, 'image_url': image_url,
                'read_more_url': read_more_url, 'title': title, 'inshort_url': inshort_url}

        news['Articles'].append(data)

    return news
