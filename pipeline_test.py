#import dlt
from dlt.destinations.qdrant import qdrant_adapter
from dlt.common import json
import pandas as pd
import camelot
import dlt
from sqlalchemy import create_engine
from typing import List

import dlt
from dlt.sources.credentials import ConnectionStringCredentials
from dlt.common import pendulum
import os

QDRANT_KEY = os.getenv('QDRANT_KEY')


from sql_database import sql_database, sql_table

def sql_database_first():
    # Get SQL Database
    credentials = ConnectionStringCredentials(
        "mysql+pymysql://rfamro@mysql-rfam-public.ebi.ac.uk:4497/Rfam"
    )
    data_sql = sql_table(credentials=credentials, table = "family")

    # Create a pipeline
    pipeline = dlt.pipeline(
        pipeline_name="test", destination='duckdb', dataset_name="rfam_data"
    )

    # Run the pipeline to load SQL db
    info = pipeline.run(data_sql, table_name="family", write_disposition="merge", primary_key="rfam_acc")
    print(info)

    pipeline2 = dlt.pipeline(
        pipeline_name="test2", destination='duckdb', dataset_name="rfam_data"
    )

    # Run the pipeline to load SQL db
    info = pipeline2.run(data_sql, table_name="family", write_disposition="replace")
    print(info)

    # Run the pipeline to update SQL db
#    info = pipeline.run(data_csv, table_name="family", write_disposition="merge", primary_key="rfam_acc")    
#    print(info)

def json_csv():
    # Create a pipeline
    pipeline = dlt.pipeline(
        pipeline_name='quick_start', destination='duckdb', dataset_name='mydata'
    )

    # Get the json file
    with open("./sources_samples/sample1.json", 'rb') as file:
        data_json = json.load(file)

    # Get the csv file
    df = pd.read_csv("sources_samples/sample3.csv")
    data_csv = df.to_dict(orient='records')

    # Run the pipleine to load json data
    load_info = pipeline.run(data_json, table_name="users", write_disposition="replace")
    print(load_info)
    
    # Run the pipeline to update json data with data in the csv file
    load_info = pipeline.run(data_csv, table_name="users", write_disposition="merge", primary_key="rfam_acc")
    print(load_info)

# This makes sure the main function is called when the script is run directly
if __name__ == "__main__":
    sql_database_first()
    #json_csv()