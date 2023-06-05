black:
	black -l 120 foods django_test_project

isort:
	isort --profile black foods django_test_project

flake8:
	flake8 --max-line-length 120 foods django_test_project

format: black isort

lint: flake8
