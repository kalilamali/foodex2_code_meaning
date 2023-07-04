# foodex2_code_meaning
This program takes an EFSA FoodEx2 code and returns its meaning.

This program is a complement to the search bar at https://data.food.gov.uk/codes/

At https://data.food.gov.uk/codes/ you can search for a food using its name. For example: **Chocolate/cocoa-based products**\
However you can't do a food search using its code: For example: **A0EQS**

## Try it online:
https://kalilamali-foodex2-code-meaning-app-wr56ng.streamlitapp.com/

<img src="https://github.com/kalilamali/foodex2_code_meaning_app/blob/main/app_image.png" width="500"/>

## Installation
```bash
git clone https://github.com/kalilamali/foodex2_code_meaning_app.git
cd foodex2_code_meaning_app
# You can install the requirements with pip:
pip install -r requirements.txt
# ... or with conda:
conda create --name streamlit_playground --file ./requirements.txt
conda activate streamlit_playground
```
## How-to run
```bash
streamlit run app.py
```
## CITATION
If you find this repository useful please cite:

Loaiza, K. (2022). FoodEx2 Code Meaning App. (Version 1.0) [Computer software]. https://github.com/kalilamali/foodex2_code_meaning_app

## LICENSE
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
