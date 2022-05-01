DB_NAME = postgres-sqlalchemy

run-postgres:
	docker run -d -p 5432:5432 --name ${DB_NAME} -e POSTGRES_PASSWORD=1234 --rm postgres 

attach_postgres:
	docker exec -it ${DB_NAME} psql -U postgres

clean-up:
	docker kill ${DB_NAME}

restart-postgres:
	make clean-up
	make run-postgres

format:
	black .
	isort .
