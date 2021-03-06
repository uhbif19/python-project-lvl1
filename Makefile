.PHONY: install brain-games build publish lint
install:
	poetry install
brain-games:
	poetry run brain-games
brain-even:
	poetry run brain-even
brain-calculator:
	poetry run brain-calculator
brain-gcd:
	poetry run brain-gcd
brain-progression:
	poetry run brain-progression
brain-prime:
	poetry run brain-prime
test:
	poetry run pytest
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 brain_games tests
