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

from sql_database import sql_database, sql_table
from qdrant_client import QdrantClient

def json_csv():
    # Create a pipeline
    pipeline = dlt.pipeline(
        pipeline_name='qdrant5', destination='qdrant', dataset_name='mydata'
    )

    # Get the json file
    with open("./sources_samples/sample1.json", 'rb') as file:
        data_json = json.load(file)

    all_fields_json = list(data_json[0].keys())

    info = pipeline.run(
        qdrant_adapter(
            data_json,
            embed=all_fields_json,
        )
    )

    print(info)

    pipeline2 = dlt.pipeline(
        pipeline_name='qdrant6', destination='qdrant', dataset_name='mydata'
    )


    # Get the csv file
    df = pd.read_csv("sources_samples/sample3.csv")
    data_csv = df.to_dict(orient='records')
    all_fields_csv = list(data_csv[0].keys())

    info = pipeline2.run(
        qdrant_adapter(
            data_csv,
            embed=all_fields_csv,
        ),
    primary_key="rfam_acc",
    write_disposition="merge"
    )

    print(info)

# This makes sure the main function is called when the script is run directly
if __name__ == "__main__":
    #json_csv()

    # Connect to Qdrant
    qdrant_client = QdrantClient(
        "https://3ad0d7d5-4015-4ccc-b8d5-c09f8121bd2b.us-east4-0.gcp.cloud.qdrant.io",
        api_key="GP2xb22FrO1cMMBBcaxkGJHzWHBBf86yms7u48Sxjco1LoENfXlo8Q",
    )

    result = qdrant_client.query(
        collection_name="mydata_content",
        query_text="Who is an avid reader and writer?"
    )

    print(result)
