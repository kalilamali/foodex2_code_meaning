"""
This function takes an EFSA FoodEx2 code and returns its meaning.
More info about EFSA FoodEx2 codes here:
https://www.wikidata.org/wiki/Property:P4637
"""
# Created date: 05-08-2022
# Author: Karen Loaiza

# Libraries
import requests
from bs4 import BeautifulSoup


# Functions
def get_meaning_foodex2_code(code):
    try:
        url = f"https://data.food.gov.uk/codes/foodtype/id/{code}"
        r = requests.get(url, timeout=5)
        print(f"Status Code: {r.status_code}")
        html_string = r.content.decode("utf-8")
        soup = BeautifulSoup(html_string, features="lxml")
        description = soup.find(id="description").h2.get_text()
        meaning = description.split(':')[1]
        meaning = meaning.strip()
        return meaning
    except KeyError:
        error_msg = f"Description not found in {url}"
        return error_msg
