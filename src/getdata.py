import requests
from bs4 import BeautifulSoup as soup
import json
import csv
import os

nikkei = './src/data/nikkei_stock_average_par_value_en.csv'

def get_constituent_list():
    instruments = []
    with open(nikkei, 'rt') as fin:
        constituents = csv.reader(fin)
        instruments = [row for row in constituents]

    for instrument in instruments:
        instrument[0] = instrument[0] + ':JP'
    
    return instruments

def get_id(insturments):
    id_list = []
    for insturment in insturments:
        id_list.append(insturment[0])

    return id_list


def get_constituents_prev_close_price(constituents):
    """get previous close prices in each constituent"""
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
