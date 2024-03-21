import pandas as pd
from sqlalchemy import create_engine



# Define source and destination details

source_connection_string = "sqlite:///source.db"  # Replace with your source connection string (e.g., CSV, database)
destination_connection_string = "sqlite:///destination.db"  # Replace with your destination connection string (database)
source_table = "users"  # Replace with your source table name
destination_table = "users"  # Replace with your destination table name



# Extract data from the source

def extract_data_from_source1():
    engine = create_engine(source_connection_string)
    source_1 = pd.read_sql_query(f"SELECT * FROM {source_table}", engine)
    return source_1

def extract_data_from_source2():
    engine = create_engine(source_connection_string)
    source_2 = pd.read_sql_query(f"SELECT * FROM {source_table}", engine)
    return source_2 



# Transform data (cleaning, calculations, etc.)

def transform_data(data_from_source1, data_from_source2):
    # Perform data cleaning, standardization, calculations, etc.
    transformed_data = data_from_source1.copy()  # Avoid modifying the original DataFrame
    transformed_data["new_column"] = data_from_source1["existing_column"] * 2  # Example transformation
    return transformed_data



# Load data to the destination

def load_data(transformed_data):
    # Load data to the destination using SQLAlchemy
    destination_engine = create_engine(destination_connection_string)
    transformed_data.to_sql(destination_table, destination_engine, index=False, if_exists='replace')
    return transformed_data



def run_etl():
    # Call extract, transform, and load functions in sequence
    data_from_source1 = extract_data_from_source1()
    data_from_source2 = extract_data_from_source2()
    # ... extract from other sources if needed

    transformed_data = transform_data(data_from_source1, data_from_source2, ...)

    load_data(transformed_data)

    print("ETL process completed successfully!")