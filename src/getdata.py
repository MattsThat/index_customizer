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
        tags = soup(page)
        label_tags = tags.find_all('div', class_='cell__label')
        close_tag = label_tags[3]
        value_tags = tags.find_all('div', class_='cell__label')
        price_tag = value_tags[3]
        result = [close_tag, price_tag]
    
    return result


        

