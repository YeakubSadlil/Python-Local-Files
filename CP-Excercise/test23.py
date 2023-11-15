def findMaximumProfit(category, price):
    n = len(category)
    
    # Create a list of tuples (category, price) and sort it by price in descending order
    items = [(category[i], price[i]) for i in range(n)]
    items.sort(key=lambda x: x[1], reverse=True)
    
    total_profit = 0
    category_count = {}
    
    for cat, pri in items:
        if cat not in category_count:
            category_count[cat] = 0
        category_count[cat] += 1
        profit = pri * category_count[cat]
        total_profit += profit
    
    return total_profit

# Input
n = int(input())
category = [int(input()) for _ in range(n)]
price = [int(input()) for _ in range(n)]

# Call the function and print the result
result = findMaximumProfit(category, price)
print(result)
