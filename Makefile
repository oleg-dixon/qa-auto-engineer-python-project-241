install:
	uv sync

help:
	@echo "gendiff -h"
	@uv run -- gendiff -h

FILE1 ?= gendiff/tests/fixtures/file1.json
FILE2 ?= gendiff/tests/fixtures/file2.json

difference:
	@echo "Using files: $(FILE1) and $(FILE2)"
	@test -f $(FILE1) || (echo "Error: $(FILE1) not found"; exit 1)
	@test -f $(FILE2) || (echo "Error: $(FILE2) not found"; exit 1)
	uv run -- gendiff $(FILE1) $(FILE2)

build:
	uv build

test:
	uv run pytest

test-coverage:
	uv run pytest --cov

package-install:
	uv tool install dist/*.whl

package-reassemble:
	uv tool install --force dist/*.whl

check-lint:
	uv run ruff check gendiff

fix-lint:
	uv run ruff check --fix gendiff