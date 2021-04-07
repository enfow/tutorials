format:
	black .
	isort .

lint:
	env PYTHONPATH=. pytest --flake8 --pylint

setup:
	pip install -r requirements.txt
