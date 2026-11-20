# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food_expenses = sum(week[0] for week in monthly_expenses)
transport_expenses = sum(week[1] for week in monthly_expenses)
utilities_expenses = sum(week[2] for week in monthly_expenses)

week1_expenses = sum(monthly_expenses[0])
week2_expenses = sum(monthly_expenses[1])
week3_expenses = sum(monthly_expenses[2])
week4_expenses = sum(monthly_expenses[3])

total_expenses = 0
for week in monthly_expenses:
   total_expenses += sum(week)

# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_expenses)
print('Transport:', transport_expenses)
print('Utilities:', utilities_expenses)
print('Week 1:', week1_expenses)
print('Week 2:', week2_expenses)
print('Week 3:', week3_expenses)
print('Week 4:', week4_expenses)
print('---------------')
print('TOTAL:', total_expenses)