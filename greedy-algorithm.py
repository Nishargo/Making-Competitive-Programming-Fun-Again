# let's consider an example: the Coin Change Problem.
def coin_change_greedy(coins, amount):
    # Sort the coins in descending order
    # The reverse=True parameter in the sort function is used to sort the list in descending order.  
    # For example, if coins is [1, 2, 5, 10, 25], it will be sorted to [25, 10, 5, 2, 1].
    coins.sort(reverse=True)
    
    # Initialize the result list
    result = []
    
    # Iterate over each coin
    for coin in coins:
        # Find the maximum number of coins of this denomination
        count = amount // coin
        # Add those coins to the result list
        result.extend([coin] * count)
        # Decrease the amount by the total value of these coins
        amount -= coin * count
    
    # Check if the amount has been successfully changed
    if amount != 0:
        return None  # No solution found
    else:
        return result

# Example usage
coins = [1, 2, 5, 10, 25]
amount = 37

change = coin_change_greedy(coins, amount)
if change:
    print(f"The minimum number of coins to make {amount} is: {change}")
else:
    print(f"It is not possible to make {amount} with the given coin denominations.")

