run:
	python -m labyrinthe.main

test:
	pytest tests/

lint:
	flake8 labyrinthe/
