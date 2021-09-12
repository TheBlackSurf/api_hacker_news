import requests
from operator import itemgetter
from bs4 import BeautifulSoup
from requests import get

print("""

 __   __  __  ___  __   __   __  __                               __                      
/ _` |__)  / |__  / _` /  \ |__)  /    |__/  /\  |     |\/| |  | /__`                     
\__> |  \ /_ |___ \__> \__/ |  \ /_    |  \ /~~\ |___  |  | \__/ .__/                     
                                                                                          

""")


def new_stories():
    best = input("""
    You want reading BestStories article, type best
    You want reading NewsStories article, type new
    You want reading TopStories article, type top
    """)
    
    if best != 'best' and best != 'new' and best != 'top':
        new_stories()
    else:
        url = 'https://hacker-news.firebaseio.com/v0/'+best+'stories.json'
        r = requests.get(url)
        hacknews_ids = response_dict = r.json()
        hacknews_dicts = []

        for hacknews_id in hacknews_ids[:5]:
            url = f"https://hacker-news.firebaseio.com/v0/item/{hacknews_id}.json"
            r = requests.get(url)
            response_dict = r.json()

            try:
                hacknews_dict = {
                    'title': response_dict['title'],
                    'link': f"https://hacker-news.firebaseio.com/v0/item/{hacknews_id}.json",
                    'comments': response_dict['descendants'],
                    'url_real': response_dict['url'],
                }
                hacknews_dicts.append(hacknews_dict)
            except KeyError:
                continue

        hacknews_dicts = sorted(hacknews_dicts, key=itemgetter('comments'), reverse=True)

        for hacknews_dict in hacknews_dicts:
            print('=========================')
            print('=========================')

            print(f"Title: {hacknews_dict['title']}")
            print(f"URL_REAL: {hacknews_dict['url_real']}")
            print(f"Comments: {hacknews_dict['comments']}")
            print(f"JSON_URL: {hacknews_dict['link']}")

            print('=========================')
            print('=========================')
        new_stories()

new_stories()