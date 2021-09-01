import requests
from operator import itemgetter
from bs4 import BeautifulSoup
from requests import get

print("""

      __        ___  __   __      __   __             __        __         ___   __       
 /\  |__) |    |__  /  \ |__)    /__` /  \ |\ |  /\  |__) |__| /  \  |\/| |__   |__) |    
/~~\ |    |    |    \__/ |  \    .__/ \__/ | \| /~~\ |  \ |  | \__/  |  | |___ .|    |___ 
                                                                                          
 __   __  __  ___  __   __   __  __                               __                      
/ _` |__)  / |__  / _` /  \ |__)  /    |__/  /\  |     |\/| |  | /__`                     
\__> |  \ /_ |___ \__> \__/ |  \ /_    |  \ /~~\ |___  |  | \__/ .__/                     
                                                                                          

""")



print('=========================')
print('Hello, ready to start?')
print('=========================')
yesornot = input("""
Type 1 and enter to newstories.
=========================
Type 2 and enter to beststories.
=========================
Type 3 and enter to topstories
=========================

""")



def best_stories():
    url = 'https://hacker-news.firebaseio.com/v0/beststories.json'
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
        print(f"URL Link: {hacknews_dict['link']}")

        print('=========================')
        print('=========================')



def top_stories():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
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
        print(f"URL Link: {hacknews_dict['link']}")

        print('=========================')
        print('=========================')


def new_stories():
    url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
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
        print(f"URL Link: {hacknews_dict['link']}")

        print('=========================')
        print('=========================')




if yesornot == '1':
    new_stories()
elif yesornot == '2':
    best_stories()
elif yesornot == '3':
    top_stories()



else:
    print('I dont know, what is this')

