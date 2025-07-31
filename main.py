
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data
import configparser
import json
import argparse
import logging # Import logging

# --- Setup Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="ETL pipeline for stock data.")
    parser.add_argument("--symbol", type=str, default="AAPL", help="Stock symbol to process (e.g., AAPL, GOOGL).")
    args = parser.parse_args()
    symbol = args.symbol

    config = configparser.ConfigParser()
    config.read("config/config.ini")
    api_key = config["alpha_vantage"]["api_key"]
    db_name = config["database"]["db_name"]

    # Extract
    logging.info(f"Extracting data for {symbol}...")
    raw_data = extract_data(symbol, api_key)

    if raw_data is None:
        logging.error("Extraction failed. Halting pipeline.")
        exit(1) # Exit with a non-zero status code to indicate error

    with open(f"data/{symbol}_raw.json", "w") as f:
        json.dump(raw_data, f)

    # Transform
    logging.info("Transforming data...")
    transformed_data = transform_data(raw_data)
    transformed_data.to_csv(f"data/{symbol}_transformed.csv")

    # Load
    logging.info("Loading data to database...")
    load_data(transformed_data, db_name, symbol)

    # Visualize
    logging.info("Generating visualization...")
    from src.visualize import visualize_data
    visualize_data(transformed_data, symbol)
