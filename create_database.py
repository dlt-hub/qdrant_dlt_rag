# this is needed to import classes from other modules
# script_dir = os.path.dirname(os.path.abspath(__file__))
# # Get the parent directory of your script and add it to sys.path
# parent_dir = os.path.dirname(script_dir)
# sys.path.append(parent_dir)
from postgres.models.source_data import BaseModel




from postgres.database import Base

from sqlalchemy import create_engine, text
import psycopg2
from dotenv import load_dotenv
load_dotenv()
import os






def create_admin_engine(username, password, host, database_name):
    admin_url = f"postgresql://{username}:{password}@{host}:5432/{database_name}"
    return create_engine(admin_url)


def database_exists(username, password, host, db_name):
    engine = create_admin_engine(username, password, host, db_name)
    connection = engine.connect()
    query = text(f"SELECT 1 FROM pg_database WHERE datname='{db_name}'")
    result = connection.execute(query).fetchone()
    connection.close()
    engine.dispose()
    return result is not None


def create_database(username, password, host, db_name):
    engine = create_admin_engine(username, password, host, db_name)
    connection = engine.raw_connection()
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE {db_name}")
    cursor.close()
    connection.close()
    engine.dispose()


def create_tables(engine):
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    username = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    database_name = os.getenv('POSTGRES_DB')
    environment = os.environ.get("ENVIRONMENT")

    if environment == "local":
        host = os.getenv('POSTGRES_HOST')

    elif environment == "docker":
        host = os.getenv('POSTGRES_HOST_DOCKER')
    else:
        host = os.getenv('POSTGRES_HOST_DOCKER')

    engine = create_admin_engine(username, password, host, database_name)

    print(Base.metadata.tables)

    if not database_exists(username, password, host, database_name):
        print(f"Database {database_name} does not exist. Creating...")
        create_database(username, password, host, database_name)
        print(f"Database {database_name} created successfully.")

    create_tables(engine)