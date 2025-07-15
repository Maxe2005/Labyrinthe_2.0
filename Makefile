run:
	python -m labyrinthe.main

test:
	pytest tests/

lint:
	flake8 labyrinthe/

docs:
	rm -rf docs
	pdoc labyrinthe -o docs
