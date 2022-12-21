export DB_USER?=service
export DB_PASS?=service
export DB_NAME?=service
export DB_HOST?=localhost
export DB_PORT?=5432

PIP_INSTALL_CMD=pip install \
	-r requirements.txt

install:
	${PIP_INSTALL_CMD}

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
