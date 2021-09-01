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
Type 4 and enter to newstories with real url(To może działać).
=========================
Type 5 and enter to beststories with real link.(Nie zawsze działa)
=========================
Type 6 and enter to topstories with real link(Nie zawsze działa)
=========================
=========================
What do you think?

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
                'link': f"http://news.ycombinator.com/item?id={hacknews_id}",
                'comments': response_dict['descendants'],
            }
            hacknews_dicts.append(hacknews_dict)
        except KeyError:
            continue

        hacknews_dicts = sorted(hacknews_dicts, key=itemgetter('comments'), reverse=True)



    for hacknews_dict in hacknews_dicts:
        print('=========================')
        print('=========================')
        print(f"Title: {hacknews_dict['title']}")

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
                'link': f"http://news.ycombinator.com/item?id={hacknews_id}",
                'comments': response_dict['descendants'],
            }
            hacknews_dicts.append(hacknews_dict)
        except KeyError:
            continue

    hacknews_dicts = sorted(hacknews_dicts, key=itemgetter('comments'), reverse=True)


    for hacknews_dict in hacknews_dicts:
        print('=========================')
        print('=========================')
        print(f"Title: {hacknews_dict['title']}")

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
                'link': f"http://news.ycombinator.com/item?id={hacknews_id}",
                'comments': response_dict['descendants'],
            }
            hacknews_dicts.append(hacknews_dict)
        except KeyError:
            continue

    hacknews_dicts = sorted(hacknews_dicts, key=itemgetter('comments'), reverse=True)



    for hacknews_dict in hacknews_dicts:
        print('=========================')
        print('=========================')
        print(f"Title: {hacknews_dict['title']}")

        print(f"Comments: {hacknews_dict['comments']}")

        print(f"URL Link: {hacknews_dict['link']}")
        print('=========================')
        print('=========================')

                
def best_stories2():
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
                'link': f"http://news.ycombinator.com/item?id={hacknews_id}",
                'comments': response_dict['descendants'],
            }
            hacknews_dicts.append(hacknews_dict)
        except KeyError:
            continue

        hacknews_dicts = sorted(hacknews_dicts, key=itemgetter('comments'), reverse=True)



    for hacknews_dict in hacknews_dicts:
        print('=========================')
        print('=========================')
        print(f"Title: {hacknews_dict['title']}")
        print(f"Comments: {hacknews_dict['comments']}")
        print(f"URL Link: {hacknews_dict['link']}")
        URL = f"{hacknews_dict['link']}"
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for storylink in bs.find_all('tr', class_='athing'):
            footer = storylink.find('a', class_='storylink')
            print("URL to real post: " + footer.get('href'))
        print('=========================')
        print('=========================')

def top_stories2():
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
                'link': f"http://news.ycombinator.com/item?id={hacknews_id}",
                'comments': response_dict['descendants'],
            }
            hacknews_dicts.append(hacknews_dict)
        except KeyError:
            continue

    hacknews_dicts = sorted(hacknews_dicts, key=itemgetter('comments'), reverse=True)



    for hacknews_dict in hacknews_dicts:
        print('=========================')
        print('=========================')
        print(f"Title: {hacknews_dict['title']}")
        print(f"Comments: {hacknews_dict['comments']}")
        print(f"URL Link: {hacknews_dict['link']}")
        URL = f"{hacknews_dict['link']}"
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for storylink in bs.find_all('tr', class_='athing'):
            footer = storylink.find('a', class_='storylink')
            print("URL to real post: " + footer.get('href'))
        print('=========================')
        print('=========================')


def new_stories2():
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
                'link': f"http://news.ycombinator.com/item?id={hacknews_id}",
                'comments': response_dict['descendants'],
            }
            hacknews_dicts.append(hacknews_dict)
        except KeyError:
            continue

    hacknews_dicts = sorted(hacknews_dicts, key=itemgetter('comments'), reverse=True)



    for hacknews_dict in hacknews_dicts:
        print('=========================')
        print('=========================')
        print(f"Title: {hacknews_dict['title']}")
        print(f"Comments: {hacknews_dict['comments']}")
        print(f"URL Link: {hacknews_dict['link']}")
        URL = f"{hacknews_dict['link']}"
        page = get(URL)
        bs = BeautifulSoup(page.content, 'html.parser')
        for storylink in bs.find_all('tr', class_='athing'):
            footer = storylink.find('a', class_='storylink')
            print("URL to real post: " + footer.get('href'))
        print('=========================')
        print('=========================')
                

if yesornot == '1':
    new_stories()
elif yesornot == '2':
    best_stories()
elif yesornot == '3':
    top_stories()
elif yesornot == '4':
    new_stories2()
elif yesornot == '5':
    best_stories2()
elif yesornot == '6':
    top_stories2()


else:
    print('I dont know, what is this')

