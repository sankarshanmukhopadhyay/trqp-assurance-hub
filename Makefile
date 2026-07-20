.PHONY: validate flagship-check assurance-check evidence

validate:
	python scripts/validate_repository.py
	python scripts/validate_project_status.py
	python scripts/validate_compatibility_registry.py
	python tools/validate_examples.py
	python scripts/doc_tests.py

assurance-check: validate
	python -m pytest -q tests/test_cross_stack_negative_cases.py

evidence: assurance-check

flagship-check:
	python scripts/validate_repository.py
