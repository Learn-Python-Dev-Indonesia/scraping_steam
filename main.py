import os
import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

url = 'https://store.steampowered.com/search/?term=gta'

def get_data(url):
    r = requests.get(url)
    return r.text

# Processing Data
def parse(data):
    result = []
    soup = BeautifulSoup(data, 'html.parser')
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass
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

    with open('json_result.json', 'w') as outfile:
        json.dump(result, outfile)
    return result

def load_data():
    with open('json_result.json') as  json_file:
        data = json.load(json_file)

def output (datas : list):
    for i in datas:
        print(i)
def generate_data(result, filename):
    df = pd.DataFrame(result)
    df.to_excel(f'{filename}.xlsx', index=False)

if __name__ == '__main__':
    data = get_data(url)

    final_data = parse(data)
    namafile = input('Masukkan nama file:')
    generate_data(final_data, namafile)

    output(final_data)