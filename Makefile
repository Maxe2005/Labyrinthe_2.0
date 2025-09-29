run:
	.venv/bin/python -m labyrinthe.main

test:
	.venv/bin/python -m pytest tests/

lint:
	.venv/bin/python -m flake8 labyrinthe/

format:
	.venv/bin/python -m black labyrinthe/ tests/

docs:
	rm -rf docs
	.venv/bin/python -m pdoc labyrinthe -o docs
