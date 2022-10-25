import requests
from bs4 import BeautifulSoup
import json
import pandas

url = 'https://store.steampowered.com/search/?term=gta'

def get_data(url):
    r = requests.get(url)
    return r.text

# Processing Data
def parse(data):
    result = []
    soup = BeautifulSoup(data, 'html-parser')
    contents = soup.find('div', attrs={'id': 'search_resultsRows'})
    games = contents.find_all('a')

    for game in games:
        link = game['href']

#parsing data
        title = game.find('span', {'class': 'title'}).text
        price = game.find('div', {'class': 'col search_price  responsive_secondrow'})

        data_dict = {
        'title': title,
        'price': price,
        'link' : link,
        }

        result.append(data_dict)
    return result

if __name__ == '__main__':
    data = get_data(url)