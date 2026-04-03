POETRY_RUN = poetry run

.venv: pyproject.toml
	uv tool install poetry --force
	poetry config virtualenvs.in-project true
	poetry install
	touch .venv

install: .venv

run: .venv
	$(POETRY_RUN) python -m tests.test

debug: .venv
	$(POETRY_RUN) python -m pdb a_maze_ing.py config.txt

clean:
	rm -rf .venv .mypy_cache .pytest_cache dist
	find . -type d -name "__pycache__" -exec rm -rf {} +

lint: .venv
	$(POETRY_RUN) flake8 . --exclude='./.venv'
	$(POETRY_RUN) mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs --exclude './.venv'

lint-strict: .venv
	$(POETRY_RUN) flake8 . --exclude='./.venv'
	$(POETRY_RUN) mypy . --strict --exclude './.venv'

build: .venv
	poetry build
	cp dist/mazegen-*.tar.gz .
	cp dist/mazegen-*.whl .

.PHONY: install run debug clean lint lint-strict build
