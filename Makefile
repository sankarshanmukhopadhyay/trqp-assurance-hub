.PHONY: validate flagship-check assurance-check evidence stack-release-check stack-bootstrap stack-evaluate

validate:
	python scripts/validate_repository.py
	python scripts/validate_project_status.py
	python scripts/validate_compatibility_registry.py
	python tools/validate_examples.py
	python scripts/doc_tests.py

assurance-check: validate
	python -m pytest -q tests/test_cross_stack_negative_cases.py

evidence: assurance-check

stack-release-check: validate
	python tools/stack_validate.py --check-remote
	python -m pytest -q tests/test_stack_release_readiness.py tests/test_cross_stack_negative_cases.py tests/test_cts_determinism.py

stack-bootstrap:
	python tools/stack_bootstrap.py --clean

stack-evaluate:
	python tools/stack_evaluate.py

flagship-check:
	python scripts/validate_repository.py
