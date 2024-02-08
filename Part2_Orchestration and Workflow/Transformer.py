import pandas as pd
from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.REMOVE

    Docs: https://docs.mage.ai/guides/transformer-blocks#remove-rows
    """
    # Log the number of rows and columns before filtering
    print("Number of rows before filtering:", df.shape[0])
    print("Number of columns before filtering:", df.shape[1])

    # Filter rows where passenger_count is greater than 0 and trip_distance is greater than 0
    filtered_df = df[(df['passenger_count'] > 0) & (df['trip_distance'] > 0)]

    # Add new column lpep_pickup_date by converting lpep_pickup_datetime to a date
    filtered_df['lpep_pickup_date'] = pd.to_datetime(filtered_df['lpep_pickup_datetime']).dt.date

    # Count the number of columns in camel case
    camel_case_columns = sum(any(char.isupper() for char in column[1:]) for column in df.columns)
    print("Number of columns that need to be renamed to snake case:", camel_case_columns)

    # Rename columns in Camel Case to Snake Case
    renamed_columns = filtered_df.columns.to_series().apply(lambda x: x.lower())
    filtered_df = filtered_df.rename(columns=lambda x: x.lower())

    # Log the number of rows and columns after filtering
    print("Number of rows after filtering:", filtered_df.shape[0])
    print("Number of columns after filtering:", filtered_df.shape[1])

    # Print existing values of vendorid
    print("Existing values of vendorid:", sorted(filtered_df['vendorid'].unique()))

    # Assertions
    assert filtered_df['vendorid'].isin(filtered_df['vendorid']).all(), "Vendor ID is not one of the existing values in the column"
    assert (filtered_df['passenger_count'] > 0).all(), "Passenger count is not greater than 0"
    assert (filtered_df['trip_distance'] > 0).all(), "Trip distance is not greater than 0"

    return filtered_df


@test
def test_output(filtered_df) -> None:
    """
    Template code for testing the output of the block.
    """
    assert filtered_df is not None, 'The output is undefined'

