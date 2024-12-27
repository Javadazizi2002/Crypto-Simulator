import requests  # Library for sending HTTP requests
import matplotlib.pyplot as plt  # Library for plotting graphs (not used in this code)

class CryptoSimulator:
    def __init__(self):
        self.balance = 1000  # Initial user balance, set to $1000
        self.portfolio = {}  # Portfolio to hold cryptocurrencies and their amounts
        self.crypto_data = self.fetch_crypto_data()  # Fetch cryptocurrency data

    def fetch_crypto_data(self):
        # API endpoint to get cryptocurrency prices
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,litecoin&vs_currencies=usd"
        response = requests.get(url)  # Send a GET request to the API
        return response.json()  # Return the received data as JSON

    def buy_crypto(self, crypto, amount):
        # Function to buy cryptocurrency
        if crypto in self.crypto_data:  # Check if the cryptocurrency exists in fetched data
            price = self.crypto_data[crypto]['usd']  # Get the price of the cryptocurrency
            cost = price * amount  # Calculate the total cost of the purchase
            if cost <= self.balance:  # Check if there is enough balance
                self.balance -= cost  # Deduct the cost from the balance
                if crypto in self.portfolio:  # If the cryptocurrency is already in the portfolio
                    self.portfolio[crypto] += amount  # Increase its amount
                else:
                    self.portfolio[crypto] = amount  # If new, set its amount
                return f"Bought {amount} {crypto} for {cost} dollars."  # Success message for purchase
            else:
                return "Insufficient balance."  # Message for insufficient balance
        else:
            return "Invalid cryptocurrency."  # Message for invalid cryptocurrency

    def sell_crypto(self, crypto, amount):
        # Function to sell cryptocurrency
        if crypto in self.portfolio and self.portfolio[crypto] >= amount:  # Check if the crypto is in portfolio and enough amount exists
            price = self.crypto_data[crypto]['usd']  # Get the price of the cryptocurrency
            revenue = price * amount  # Calculate revenue from the sale
            self.balance += revenue  # Increase balance by the revenue from sale
            self.portfolio[crypto] -= amount  # Decrease the amount of crypto in portfolio
            if self.portfolio[crypto] == 0:  # If amount reaches zero, remove it from portfolio
                del self.portfolio[crypto]
            return f"Sold {amount} {crypto} for {revenue} dollars."  # Success message for sale
        else:
            return "Not enough quantity to sell."  # Message for insufficient quantity to sell

    def display_portfolio(self):
        # Function to display portfolio
        portfolio_str = "\nPortfolio:\n"  # Start string for displaying portfolio
        for crypto, amount in self.portfolio.items():  # For each cryptocurrency in portfolio
            portfolio_str += f"{crypto}: {amount}\n"  # Add crypto information to string
        portfolio_str += f"Balance: {self.balance} dollars"  # Add final balance to string
        return portfolio_str  # Return portfolio string

if __name__ == "__main__":  # Run code if the file is executed directly
    simulator = CryptoSimulator()  # Create an instance of the CryptoSimulator class

    while True:  # Infinite loop for user interaction
        print("\n1. Buy Cryptocurrency")
        print("2. Sell Cryptocurrency")
        print("3. Display Portfolio")
        print("4. Exit")

        choice = input("Choose an option: ")  # Get user choice

        if choice == '1':  # If buy option is selected
            crypto = input("Cryptocurrency name (bitcoin/ethereum/litecoin): ")  # Get cryptocurrency name
            amount = float(input("Amount to buy: "))  # Get amount to buy
            print(simulator.buy_crypto(crypto, amount))  # Call buy function and display result)
        elif choice == '2':  # If sell option is selected
            crypto = input("Cryptocurrency name (bitcoin/ethereum/litecoin): ")  # Get cryptocurrency name
            amount = float(input("Amount to sell: "))  # Get amount to sell
            print(simulator.sell_crypto(crypto, amount))  # Call sell function and display result)

        elif choice == '3':  # If display portfolio option is selected
            print(simulator.display_portfolio())  # Display portfolio

        elif choice == '4':  # If exit option is selected
            break  # Exit the loop and end the program

        else:
            print("Invalid selection.")  # Message for invalid selection

