import databases

DATABASE_URL = "postgresql://postgres:postgres@localhost/db_name"

database = databases.Database(DATABASE_URL)
