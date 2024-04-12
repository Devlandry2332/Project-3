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

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad response status
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("Error querying Alpha Vantage API:", e)
        return None

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

    if data is None:
        return  # Exit if there's an error querying the API

    # Extract dates and values 
    try:
        time_series_data = data["Time Series (Daily)"]
        dates = []
        values = []
        for date, value in time_series_data.items():
            dates.append(date)
            values.append(float(value["4. close"]))  # Assuming closing price is needed

        # Plot the graph
        plot_graph(dates, values, chart_type)
    except KeyError:
        print("Error: Unable to extract data from the response. Check if the symbol and function are correct.")

if __name__ == "__main__":
    main()