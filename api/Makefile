
psql-local:
	psql "postgres://root:thisisthelocaldatabasepassword@localhost:5432/personal-finance"

migrate-up:
	alembic upgrade head

migrate-down:
	alembic downgrade -1
