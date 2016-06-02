test: tests test-flake8

tests: install-dependencies
	coverage run setup.py test

test-flake8:
	pip install flake8
	flake8 .

install-dependencies:
	pip install -r requirements.txt
