
import pandas as pd
from sqlalchemy import create_engine
import configparser
import logging

def load_data(transformed_data, db_name, symbol):
    try:
        engine = create_engine(f"sqlite:///data/{db_name}")
        # Use the symbol as the table name for better organization
        table_name = f'{symbol}_stock_data'
        transformed_data.to_sql(table_name, engine, if_exists="replace")
        logging.info(f"Successfully loaded data for {symbol} into table {table_name} in {db_name}")
    except Exception as e:
        logging.error(f"Error loading data for {symbol} into database: {e}")

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config/config.ini")
    db_name = config["database"]["db_name"]

    # Load the transformed data from the CSV file
    transformed_data = pd.read_csv("data/transformed_stock_data.csv", index_col=0)

    # Load the data into the database
    load_data(transformed_data, db_name)
