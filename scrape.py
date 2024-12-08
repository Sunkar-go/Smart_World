import requests
from bs4 import BeautifulSoup
import pprint

current_page = 1
is_scraping = True
hn = []
hn_last=[]
def CreateCustom_hn(hn,links,votes,current_page):

    for inx, item in enumerate(links):
        href = item.a.get('href')
        title = item.a.get_text()
        try:
            points = int(votes[inx].getText().replace(' points',''))
        except IndexError:
            next(iter(enumerate(links)),None)
        if points>850:
            hn.append({'title': title, 'links': href, 'points': points, 'page': current_page})
    return hn


while is_scraping:
    res = requests.get(f"https://news.ycombinator.com/news?p={current_page}")
    soup = BeautifulSoup(res.content, 'html.parser')
    links = soup.select(".titleline")
    votes = soup.select('.score')
    next_page_scrap = soup.find(class_="morelink")
    hn_last=sorted(CreateCustom_hn(hn,links, votes,current_page), key=lambda x: x['points'], reverse=True)
    if next_page_scrap:
        current_page += 1
    else:
        print(f"Finish scraping! Total page scraped:{current_page}")
        is_scraping = False
pprint.pprint(hn_last)