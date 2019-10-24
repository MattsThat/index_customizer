import requests
from bs4 import BeautifulSoup as soup
import json
import csv

def get_information():
    pass

def get_constituents_price(constituents):
    bbg_url = 'https://www.bloomberg.co.jp/quote/'
    result = []
    for constituent in constituents:
        url = bbg_url + constituent
        response = requests.get(url)
        page = response.text
        tags = soup(page, features="html.parser")
        value_tags = tags.find_all('div', class_='cell__value')
        close_price = value_tags[3].text
        result.append([constituent, close_price])
    
    return result


        

