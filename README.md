[![Python 3.10](https://github.com/kalilamali/foodex2_code_meaning/actions/workflows/makefile.yml/badge.svg)](https://github.com/kalilamali/foodex2_code_meaning/actions/workflows/makefile.yml)

# foodex2_code_meaning
This is the repository for the foodex2_code_meaning_app. An streamlit app that takes an EFSA FoodEx2 code and returns its meaning. This app is a complement to the search bar at https://data.food.gov.uk/codes/ At https://data.food.gov.uk/codes/ you can search for a food using its name. For example: **Chocolate/cocoa-based products**\ However you can't do a food search using its code: For example: **A0EQS**

## Try it online:
Please be aware, it will take some time to wake-up the app. 
https://kalilamali-foodex2-code-meaning-app-wr56ng.streamlitapp.com/

<img src="https://github.com/kalilamali/foodex2_code_meaning_app/blob/main/app_image.png" width="500"/>

## How-to-use
```bash
git clone https://github.com/kalilamali/foodex2_code_meaning_app.git
cd foodex2_code_meaning_app
python -m venv .foodex2_code_meaning_app
source .foodex2_code_meaning_app/bin/activate
make install
make test
make run
```
## CITATION
If you find this repository useful please cite:

Loaiza, K. (2022). FoodEx2 Code Meaning App. (Version 1.0) [Computer software]. https://github.com/kalilamali/foodex2_code_meaning_app

## LICENSE
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
