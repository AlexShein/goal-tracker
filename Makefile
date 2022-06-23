
LOCAL_DB_NAME ?= local_db
LOCAL_DB_HOST ?= localhost
LOCAL_DB_PORT ?= 5432
LOCAL_DB_ADDR ?= ${LOCAL_DB_HOST}:${LOCAL_DB_PORT}/${LOCAL_DB_NAME}
LOCAL_DB_USER ?= postgres
LOCAL_DB_PASS ?= pass

POSTGRES_IMAGE = postgres
POSTGRES_TAG = 14.4
LOCAL_PKG_DIR := $(shell eval pwd)
DB_DATA_FOLDER ?= ${LOCAL_PKG_DIR}/db_data

# Code checks
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

# DB-related commands
.PHONY: db-folder
db-folder:
	mkdir -p ${DB_DATA_FOLDER}

.PHONY: rundb
rundb: ## Starts a local dev database in docker
	docker run --name ${LOCAL_DB_NAME} \
	-e POSTGRES_DB=${LOCAL_DB_NAME} \
	-e POSTGRES_PASSWORD=${LOCAL_DB_PASS} \
	-p ${LOCAL_DB_PORT}:5432 \
	--volume ${DB_DATA_FOLDER}:/var/lib/postgresql/data \
	-d ${POSTGRES_IMAGE}:${POSTGRES_TAG}

.PHONY: dbup
dbup: db-folder rundb ## Starts a local dev database in docker

.PHONY: dbdown
dbdown: ## Stops and destroys the local dev database in docker
	docker stop ${LOCAL_DB_NAME}
	docker rm ${LOCAL_DB_NAME}

.PHONY: migrate
migrate: ## Applies all unapplied DB changes
	DB_ADDR=${LOCAL_DB_ADDR} \
	DB_USER=${LOCAL_DB_USER} \
	DB_PASS=${LOCAL_DB_PASS} \
	alembic upgrade head

.PHONY: migration
migration: ## Applies all unapplied DB changes
	DB_ADDR=${LOCAL_DB_ADDR} \
	DB_USER=${LOCAL_DB_USER} \
	DB_PASS=${LOCAL_DB_PASS} \
	alembic revision --autogenerate -m $(ARGS)

.PHONY: pgcli
pgcli:
	PGPASSWORD=${LOCAL_DB_PASS} pgcli -h ${LOCAL_DB_HOST} -p ${LOCAL_DB_PORT} -U ${LOCAL_DB_USER}

run: ## Run API in reload mode so that changes are always reloaded
	DB_ADDR=${LOCAL_DB_ADDR} \
	DB_USER=${LOCAL_DB_USER} \
	DB_PASS=${LOCAL_DB_PASS} \
	poetry run uvicorn goal_tracker.app:app --reload --log-level info
