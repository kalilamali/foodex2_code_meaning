"""
This webapp takes an EFSA FoodEx2 code and returns its meaning.
More info about EFSA FoodEx2 codes here:
https://www.wikidata.org/wiki/Property:P4637
"""
# Created date: 05-08-2022
# Author: Karen Loaiza

# Libraries
import myfunctions
import streamlit as st
import pandas as pd


# Main
st.title('EFSA FoodEx2 code meaning')
st.write('Created by 👩🏻‍💻 [kalilamali](https://github.com/kalilamali)')
st.caption('This program takes an EFSA FoodEx2 code and returns its meaning.\
        More information about EFSA FoodEx2 codes can be found here:\
        https://www.wikidata.org/wiki/Property:P4637')
st.caption('Remember: An EFSA FoodEx2 code has 5 letters. For example: A02XN')

code = st.text_input('Write the code here!')
if code:
    meaning = myfunctions.get_meaning_foodex2_code(code.strip())
    
    st.write(f'Meaning: {meaning}')
