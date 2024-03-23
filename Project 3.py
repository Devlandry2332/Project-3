import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Get Symbol
def get_symbol():
    symbol = input("Enter the stock symbol you are looking for: ").upper()
    return symbol

# Get Chart Type
def get_chart_type():
    print("Chart Types")
    print("-----------")
    print("1. Bar")
    print("2. Line")
    while True:
        chart_type = input("Enter the chart type you want (1, 2): ")
        try:
            chart_type = int(chart_type)
            if chart_type in (1, 2):
                return str(chart_type)
        except ValueError:
            print("Error: Please enter 1 for Bar or 2 for Line.")

# Get Time Series
def get_time_series():
    print("Select the Time Series of the chart you want to Generate")
    print("--------------------------------------------------------")
    print("1. Intraday")
    print("2. Daily")
    print("3. Weekly")
    print("4. Monthly")
    while True:
        time_series = input("Enter the time series option (1, 2, 3, 4): ")
        try:
            time_series = int(time_series)
            if time_series in (1, 2, 3, 4):
                if time_series == 1:
                    return "TIME_SERIES_INTRADAY"
                elif time_series == 2:
                    return "TIME_SERIES_DAILY"
                elif time_series == 3:
                    return "TIME_SERIES_WEEKLY"
                else:
                    return "TIME_SERIES_MONTHLY"
        except ValueError:
            print("Error: Please enter 1 for Bar or 2 for Line.")

# Get Start Date
def get_start_date():
    while True:
        start_date = input("Enter the beginning date (YYYY-MM-DD): ")
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            return start_date
        except ValueError:
            print("Error: Please enter the date in YYYY-MM-DD format.")

# Get End Date
def get_end_date(start_date):
    while True:
        end_date = input("Enter the end date (YYYY-MM-DD): ")
        try:
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
            if end_date > start_date:
                return end_date
            else:
                print("Error End date must come after the start date.")
        except ValueError:
            print("Error: Please enter the date in YYYY-MM-DD format.")

# Function to query Alpha Vantage API
def query_alpha_vantage(symbol, function, start_date, end_date):
    api_key = "UT2CFA26ZELQE5H2" 
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
    # Inputs
    symbol = get_symbol()
    chart_type = get_chart_type()
    function = get_time_series()
    start_date = get_start_date()
    end_date = get_end_date(start_date)

    # Query Alpha Vantage API
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
