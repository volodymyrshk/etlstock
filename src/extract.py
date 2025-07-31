
import os
import requests
import configparser
import logging

def extract_data(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        logging.info(f"Successfully extracted data for {symbol}")
        return data
    except requests.exceptions.RequestException as e:
        logging.error(f"Error during API request for {symbol}: {e}")
        return None # Return None to indicate failure

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config/config.ini")
    api_key = config["alpha_vantage"]["api_key"]
    
    # Create data directory if it doesn't exist
    if not os.path.exists("data"):
        os.makedirs("data")

    # Extract data for a sample stock (e.g., AAPL)
    stock_data = extract_data("AAPL", api_key)

    # Save the extracted data to a JSON file
    with open("data/raw_stock_data.json", "w") as f:
        f.write(str(stock_data))
