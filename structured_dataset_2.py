from dlt.destinations.qdrant import qdrant_adapter
from dlt.common import json
import pandas as pd
import dlt
from dlt.destinations.qdrant import qdrant_adapter

import dlt

from sql_database import sql_database


def sql_json_pipeline():
    # Json
    with open("./synthetic_data_3/structured_dataset_2.json", 'rb') as file:
        data_json = json.load(file)
    df_json = pd.DataFrame(data_json)

    # Sql
    source = sql_database(schema='public')
    table_list = source.resources['base']
    df_sql = pd.DataFrame(table_list)

    merged_sql_json = pd.merge(df_json, df_sql, on="UserID", how="outer")
    merged = merged_sql_json.to_dict(orient="records")

    pipeline = dlt.pipeline(
        pipeline_name='structured_dataset_2_sources_pipeline_6', destination='qdrant', dataset_name='structured_dataset_2'
    )

    column_names = merged_sql_json.columns.tolist()
    print(column_names)
    
    info = pipeline.run(
        qdrant_adapter(
            merged,
            embed=column_names,
        )
    )
    print(info)    

from dlt.extract.decorators import resource as make_resource

def nested_json_pipeline():
    # Json
    with open("./synthetic_data_3/structured_dataset_2.json", 'rb') as file:
        data_json = json.load(file)
    df_json = pd.json_normalize(data_json, sep='_')

    # Sql
    source = sql_database(schema='public')
    table_list = source.resources['base']
    df_sql = pd.DataFrame(table_list)

    merged_sql_json = pd.merge(df_json, df_sql, on="UserID", how="outer")
    merged = merged_sql_json.to_dict(orient="records")

    column_names = merged_sql_json.columns.tolist()

    pipeline = dlt.pipeline(
        pipeline_name='pipeline_2', destination='qdrant', dataset_name='structured_dataset_2'
    )

    info = pipeline.run(
        qdrant_adapter(
            merged,
            embed=column_names,
        )
    )
    print(info)  

def nested_json_pipeline():
    # Json
    with open("./synthetic_data_3/structured_dataset_2.json", 'rb') as file:
        data_json = json.load(file)
    df_json = pd.json_normalize(data_json, sep='_')

    # Sql
    source = sql_database(schema='public')
    table_list = source.resources['base']
    df_sql = pd.DataFrame(table_list)

    merged_sql_json = pd.merge(df_json, df_sql, on="UserID", how="outer")
    data = merged_sql_json.to_dict(orient="records")

    column_names = merged_sql_json.columns.tolist()








    # Define your pipeline
    pipeline = dlt.pipeline(
        pipeline_name='qdrant_pipeline', destination='qdrant', dataset_name='structured_dataset_2'
    )

    # Load your data
    info = pipeline.run(
        qdrant_adapter(
            data,
            embed=["Whatever columns you want"],
        )
    )







    print(info)  


if __name__ == "__main__":
    #sql_json_pipeline()
    nested_json_pipeline()