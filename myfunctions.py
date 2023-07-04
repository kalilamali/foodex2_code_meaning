"""
This function takes an EFSA FoodEx2 code and returns its meaning.
More info about EFSA FoodEx2 codes here:
https://www.wikidata.org/wiki/Property:P4637
"""
# Created date: 05-08-2022
# Author: Karen Loaiza

# Libraries
import requests
import pandas as pd
import io


# Functions
def get_meaning_foodex2_code(code):
    try:
        url = f"https://data.food.gov.uk/codes/foodtype/id/{code}"
        r = requests.get(url)
        csv_string = r.content.decode("utf-8")
        csv_file = io.StringIO(csv_string)
        df = pd.read_csv(csv_file)
        df['skos:prefLabel'] = df['skos:prefLabel'].astype(str)
        meaning = df['skos:prefLabel'][0].strip('@en')
        meaning = meaning.strip()
        return meaning
    except KeyError:
        error_msg = f'Description not found in {url}'
        return error_msg

# Test
#print(get_meaning_foodex2_code('A02XN'))
