.PHONY: validate flagship-check

validate:
	python scripts/validate_repository.py
	python tools/validate_examples.py
	python scripts/doc_tests.py

flagship-check:
	python scripts/validate_repository.py
