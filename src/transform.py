
import json
import pandas as pd
import logging

def transform_data(raw_data):
    try:
        time_series = raw_data["Time Series (Daily)"]
    except KeyError:
        logging.error("Could not find 'Time Series (Daily)' in the raw data. The API response may have changed or an error occurred.")
        logging.error(f"API Response: {raw_data}")
        raise # Re-raise the exception to stop the pipeline

    df = pd.DataFrame.from_dict(time_series, orient="index")
    df = df.rename(columns={
        "1. open": "open",
        "2. high": "high",
        "3. low": "low",
        "4. close": "close",
        "5. volume": "volume"
    })
    df.index = pd.to_datetime(df.index)
    df = df.astype(float)

    # Clean missing values
    df = df.dropna()

    # Calculate daily returns
    df["daily_return"] = df["close"].pct_change()

    # Calculate moving averages
    df["20_day_ma"] = df["close"].rolling(window=20).mean()
    df["50_day_ma"] = df["close"].rolling(window=50).mean()

    return df

if __name__ == "__main__":
    # Load the raw data from the JSON file
    with open("data/raw_stock_data.json", "r") as f:
        raw_data = json.load(f)

    # Transform the data
    transformed_data = transform_data(raw_data)

    # Save the transformed data to a CSV file
    transformed_data.to_csv("data/transformed_stock_data.csv")
