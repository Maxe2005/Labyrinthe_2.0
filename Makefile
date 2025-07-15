run:
	python -m labyrinthe.main

test:
	pytest tests/

lint:
	flake8 labyrinthe/

docs:
	pdoc --html labyrinthe --output-dir docs --force
