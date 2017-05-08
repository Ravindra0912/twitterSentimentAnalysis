import requests
from bs4 import BeautifulSoup
from queue import *

q = Queue()
def c_spider():
    url = 'http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"lxml")
    none = 0
    movies = []
    for link in soup.findAll('h4',{'itemprop':'name'}):
        title= link.get('title')
        none += 1
        title=link.string
        if(none > 8 and none < 15):
            if(title != " None "):
                print(title)
                q.put(title)

    i =0
    # print(none)
    print(q.get(i))
c_spider()