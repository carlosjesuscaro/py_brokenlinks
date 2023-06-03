# importing libraries
import requests
from bs4 import BeautifulSoup

"Goal: to identify broken child links from a parent link"

def collect_urls():
    #url = "https://www.crummy.com/software/BeautifulSoup/"
    url = "http://peru21.pe"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, features="html.parser")
            urls = []
            [urls.append(link.get('href')) for link in soup.find_all('a')]
            print(urls)
        else:
            print("Not a 200")
    except:
        print("There was a mess!")

if __name__ == '__main__':
    collect_urls()