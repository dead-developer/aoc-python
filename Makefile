# Python test automation Makefile
.PHONY: test clean help

# Default target
.DEFAULT_GOAL := help

# Python and test settings
PYTHON = python
TEST_RUNNER = pytest
TEST_ARGS = -v

# Find all Python test files recursively
TEST_FILES = $(shell dir /s /b test_*.py 2>nul)

help:
	@echo Available commands:
	@echo   make test  - Run all Python tests in subfolders
	@echo   make clean - Clean up Python cache files
	@echo   make help  - Show this help message

test:
	$(PYTHON) -m $(TEST_RUNNER) $(TEST_ARGS) $(TEST_FILES)

clean:
	@echo Cleaning Python cache files...
	@del /s /q *.pyc 2>nul || exit 0
	@del /s /q *.pyo 2>nul || exit 0
	@del /s /q __pycache__\* 2>nul || exit 0
	@rmdir /s /q __pycache__ 2>nul || exit 0
	@echo Cleanup complete!
