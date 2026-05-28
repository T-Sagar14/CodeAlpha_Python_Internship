# Dictionary containing stock prices

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 170,
    "MSFT": 330
}

# Variable to store total investment value
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")

# Ask user how many stocks they own
num_stocks = int(input("Enter number of stocks you own: "))

# Loop for each stock
for i in range(num_stocks):

    # Input stock symbol
    stock_name = input("\nEnter stock symbol: ").upper()

    # Input quantity
    quantity = int(input("Enter quantity: "))

    # Check if stock exists
    if stock_name in stock_prices:

        # Calculate stock value
        stock_value = stock_prices[stock_name] * quantity

        # Add to total investment
        total_investment += stock_value

        # Display stock value
        print(f"{stock_name} Value = ${stock_value}")

    else:
        print("❌ Stock not found in database.")

# Display total investment
print("\n💰 Total Investment Value = $", total_investment)
