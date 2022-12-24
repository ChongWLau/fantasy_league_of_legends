LINT_FILES=fantasy_league_of_legends/ features/ tests/ run_api.py

export DB_USER?=service
export DB_PASS?=service
export DB_NAME?=service
export DB_HOST?=localhost
export DB_PORT?=5432

PIP_INSTALL_CMD=pip install \
	-r requirements.txt

PIP_INSTALL_TEST=pip install \
	-r requirements-test.txt

install:
	${PIP_INSTALL_CMD}

test_install:
	${PIP_INSTALL_TEST}

pytest:
	python -m pytest tests/

behave:
	behave features --stop

mypy:
	mypy ${LINT_FILES}

lint: mypy
	black ${LINT_FILES}
	isort --profile black ${LINT_FILES}
	flake8 ${LINT_FILES}

coverage:
	coverage run --omit="*/test*,*/app.py" -m pytest tests
	coverage run --omit="features/*,*/app.py,*__init__.py" --append -m behave
	coverage report
	coverage html

test: lint coverage

up:
	docker-compose up -d

down:
	docker-compose down

service:
	python run_api.py

create-migration:
	migrate create -dir migrations -ext sql $(name)

migrate-up:
	migrate -path=./migrations/ -database=postgres://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=disable up $(n)

migrate-force:
	migrate -path=./migrations/ -database=postgres://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=disable force $(version)

migrate-down:
	migrate -path=./migrations/ -database=postgres://${DB_USER}:${DB_PASS}@${DB_HOST}:${DB_PORT}/${DB_NAME}?sslmode=disable down $(n)

sql-lint:
	sqlfluff lint --dialect postgres migrations/

sql-fix:
	sqlfluff fix --dialect postgres migrations/
