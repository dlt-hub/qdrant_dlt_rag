import os

from sqlalchemy import create_engine

from postgres.helpers import session_scope, add_entity
from postgres.database import AsyncSessionLocal
from postgres.models.source_data import BaseModel
import uuid

import pandas as pd
from dotenv import load_dotenv
load_dotenv()

pd.set_option('display.max_colwidth', None)
async def main():


    df = pd.read_csv("synthetic_data_3/structured_dataset_1.csv")

    #PostgreSQL database
    username = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    database_name = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_HOST')
    engine = create_engine(f'postgresql+psycopg2://{username}:{password}@{host}:5432/{database_name}')

    # Write the DataFrame to SQL
    df.to_sql('base', con=engine, if_exists='replace', index=False)



if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
