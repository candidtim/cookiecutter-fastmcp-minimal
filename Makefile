all: test

clean:
	rm -rf /tmp/mymcp/

test:
	rm -rf /tmp/mymcp/ && \
	cookiecutter . --output-dir /tmp --replay --replay-file test-config.json && \
	cd /tmp/mymcp && \
	uv lock && \
	uv sync && \
	uv run pytest && \
	uv run ruff check && \
	uv run ruff format --check && \
	uv run mypy
