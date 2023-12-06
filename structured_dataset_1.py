from typing import List
from dlt.destinations.qdrant import qdrant_adapter

import dlt

from sql_database import sql_database
import os

QDRANT_KEY = os.getenv('QDRANT_KEY')

def sql_pipeline():
    source = sql_database(schema='public')
    table_list = source.resources['base']

    for data_row in table_list:
        column_names = list(data_row.keys())
        break

    pipeline = dlt.pipeline(
        pipeline_name="structured_dataset_1_sql", destination='qdrant', dataset_name="structured_dataset_1"
    )

    info = pipeline.run(
        qdrant_adapter(
            table_list,
            embed=column_names,
        )
    )

    print(info)

if __name__ == "__main__":
    sql_pipeline()