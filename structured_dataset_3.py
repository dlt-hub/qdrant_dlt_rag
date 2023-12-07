from dlt.destinations.qdrant import qdrant_adapter
from dlt.common import json
import pandas as pd
import dlt
from dlt.destinations.qdrant import qdrant_adapter

import dlt

from sql_database import sql_database


def json_csv_sql_pipeline():
    # Json
    with open("./synthetic_data_3/structured_dataset_2.json", 'rb') as file:
        data_json = json.load(file)
    df_json = pd.json_normalize(data_json, sep='_')

    # Csv 
    df_csv = pd.read_csv("synthetic_data_3/structured_dataset_3.csv")

    # Sql
    source = sql_database(schema='public')
    table_list = source.resources['base']
    df_sql = pd.DataFrame(table_list)

    merged_json_csv = pd.merge(df_json, df_csv, on="UserID", how="outer")
    merged_json_csv_sql = pd.merge(merged_json_csv, df_sql, on="UserID", how="outer")
    merged = merged_json_csv_sql.to_dict(orient="records")

    pipeline = dlt.pipeline(
        pipeline_name='pipeline_3', destination='qdrant', dataset_name='structured_dataset_3'
    )

    column_names = merged_json_csv_sql.columns.tolist()
    
    info = pipeline.run(
        qdrant_adapter(
            merged,
            embed=column_names,
        )
    )
    print(info)

if __name__ == "__main__":
    json_csv_sql_pipeline()