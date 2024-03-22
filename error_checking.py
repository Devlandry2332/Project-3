import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Function to query Alpha Vantage API
def query_alpha_vantage(symbol, function, start_date, end_date):
    api_key = "OUR API KEY"  # Replace with our Alpha Vantage API key
    base_url = "https://www.alphavantage.co/query"

    params = {
        "function": function,
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "full",  # Retrieve full data for the range selected
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

# Function to plot the graph
def plot_graph(dates, values, chart_type):
    plt.figure(figsize=(10, 6))
    plt.plot(dates, values)
    plt.title(f"Stock Data ({chart_type})")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Main function (enter inputs)
def main():
    symbol = input("Enter the stock symbol: ").upper()
    function = input("Enter the time series function (e.g., TIME_SERIES_DAILY): ")
    chart_type = input("Enter the chart type (e.g., line, bar): ").lower()
    start_date = input("Enter the beginning date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Validate dates
    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        if end_date < start_date:
            print("Error: End date cannot be before the start date.")
            return
    except ValueError:
        print("Error: Invalid date format.")
        return

    data = query_alpha_vantage(symbol, function, start_date, end_date)

    # Extract dates and values 
    dates = []
    values = []
    for date, value in data["Time Series (Daily)"].items():
        dates.append(date)
        values.append(float(value["4. close"]))  # Assuming closing price is needed

    # Plot the graph
    plot_graph(dates, values, chart_type)

if __name__ == "__main__":
    main()