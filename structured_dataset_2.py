from dlt.destinations.qdrant import qdrant_adapter
from dlt.common import json
import pandas as pd
import dlt
from dlt.destinations.qdrant import qdrant_adapter

import dlt

from sql_database import sql_database

def json_csv_pipeline():
    with open("./synthetic_data/structured_dataset_2.json", 'rb') as file:
        data_json = json.load(file)
    df_json = pd.DataFrame(data_json)

    df_csv = pd.read_csv("synthetic_data/structured_dataset_3.csv")

    merged_df = pd.merge(df_json, df_csv, on="Unique ID", how="outer")
    merged_df.reset_index(drop=True, inplace=True)

    pipeline = dlt.pipeline(
        pipeline_name='structured_dataset_2_json_csv', destination='qdrant', dataset_name='structured_dataset_2'
    )

    column_names = merged_df.columns.tolist()
    
    info = pipeline.run(
        qdrant_adapter(
            data_json,
            embed=column_names,
        )
    )
    print(info)

if __name__ == "__main__":
    json_csv_pipeline()