"""
This function takes an EFSA FoodEx2 code and returns its meaning.
More info about EFSA FoodEx2 codes here:
https://www.wikidata.org/wiki/Property:P4637
"""
# Created date: 05-08-2022
# Author: Karen Loaiza

# Libraries
import urllib.request as ur
from bs4 import BeautifulSoup
import pandas as pd

def get_meaning_foodex2_code(code):
    url = f"https://data.food.gov.uk/codes/foodtype/id/{code}"
    with ur.urlopen(url) as i:
        html_doc = i.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    try:
        description = soup.find(id="description").h2.get_text()
        meaning = description.split(':')[1]
        meaning = meaning.strip()
        return meaning
    except AttributeError:
        error_msg = f'Description not found in {url}'
        return error_msg

# Test
#print(get_meaning_foodex2_code('A02XN'))