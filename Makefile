install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
run:
	streamlit run app.py
lint:
	pylint --disable=R,C *.py
format:
	black *.py
test:
	python -m pytest -vv test_*.py
