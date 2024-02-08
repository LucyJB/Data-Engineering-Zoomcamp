import io
import pandas as pd
import requests
import gzip
from pandas import DataFrame

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(**kwargs) -> DataFrame:
    """
    Template for loading data from API
    """
    urls = [
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz',
        'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz'
    ]

    dfs = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            # Decompress the gzip content
            decompressed_content = gzip.decompress(response.content)
            # Read the CSV content using pd.read_csv
            df = pd.read_csv(io.BytesIO(decompressed_content))
            dfs.append(df)
        else:
            print(f"Failed to fetch data from {url}")

    if dfs:
        return pd.concat(dfs, ignore_index=True)
    else:
        return pd.DataFrame()  # Return an empty DataFrame if no data is loaded

@test
def test_output(df) -> None:
    """
    Template code for testing the output of the block.
    """
    assert df is not None, 'The output is undefined'
    assert not df.empty, 'The output DataFrame is empty'
