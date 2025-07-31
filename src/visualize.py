
import pandas as pd
import matplotlib.pyplot as plt
import os

def visualize_data(df, symbol):
    """Generates and saves a plot of stock prices and moving averages."""
    if not os.path.exists("output"):
        os.makedirs("output")

    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['close'], label='Close Price')
    plt.plot(df.index, df['20_day_ma'], label='20-Day MA')
    plt.plot(df.index, df['50_day_ma'], label='50-Day MA')
    plt.title(f'{symbol} Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    
    # Save the plot
    output_path = os.path.join("output", f"{symbol}_price_and_ma.png")
    plt.savefig(output_path)
    print(f"Chart saved to {output_path}")

if __name__ == "__main__":
    # This part is for standalone testing of the script
    # It assumes the transformed data for AAPL is available
    try:
        transformed_data = pd.read_csv("data/transformed_stock_data.csv", index_col=0, parse_dates=True)
        visualize_data(transformed_data, "AAPL")
    except FileNotFoundError:
        print("Transformed data not found. Please run the main pipeline first.")
