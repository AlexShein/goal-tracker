dev-run: ## Run API in reload mode so that changes are always reloaded
	poetry run uvicorn goal_tracker.app:app --reload --log-level info

lint: ## Lint the code using pylint
	poetry run pylint --rcfile .pylintrc goal_tracker/ tests/

black: ## Format code using black
	poetry run black -t py310 -l 110 goal_tracker/ tests/

isort: ## Sort python imports using isort
	poetry run isort goal_tracker/ tests/

mypy: ## Check static typing in code
	poetry run mypy --config-file mypy.ini goal_tracker/ tests/

.PHONY: check
checks: isort mypy black lint