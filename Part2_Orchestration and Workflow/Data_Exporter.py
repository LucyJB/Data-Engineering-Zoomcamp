import pandas as pd
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path
import psycopg2
from io import StringIO

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'moonpig-hello-cat-camera'  # Replace with your bucket name
    object_key = 'green_taxi/{date}/part_{part}.parquet'  # Adjust the object key format as needed

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        bucket_name,
        object_key,
    )

def export_to_postgres(df: DataFrame, table_name: str, replace_table: bool = True):
    """
    Export DataFrame to a PostgreSQL table.
    """
    # Define your PostgreSQL connection parameters
    dbname = 'postgres'      # Replace with your database name
    user = 'username'       # Replace with your username
    password = 'password'   # Replace with your password
    host = 'hostname'           # Replace with your host (usually localhost or an IP address)
    port = '5432'           # Replace with your port (usually 5432)

    # Connect to PostgreSQL
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # If replace_table is True, drop the table if it exists
    if replace_table:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Create the table based on DataFrame columns
    columns = ', '.join(df.columns)
    cursor.execute(f"CREATE TABLE {table_name} ({columns})")

    # Use StringIO to handle DataFrame as CSV and copy data to PostgreSQL table
    output = StringIO()
    df.to_csv(output, sep='\t', header=False, index=False)
    output.seek(0)
    cursor.copy_from(output, table_name, null='')
    conn.commit()

    # Close connection
    cursor.close()
    conn.close()

# Usage
# Make sure you have your DataFrame `df` defined before calling these functions
# Example usage:
# export_to_postgres(df, table_name='mage.green_taxi', replace_table=True)
# export_data_to_google_cloud_storage(df)
