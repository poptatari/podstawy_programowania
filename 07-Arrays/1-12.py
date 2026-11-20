# This program calculates the most expensive category from a list of expenses.

categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

most_expensive = max(expenses)
most_expensive_index = expenses.index(most_expensive)
print("The most expensive category is:", categories[most_expensive_index])