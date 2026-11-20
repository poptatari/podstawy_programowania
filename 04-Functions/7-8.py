# Function to calculate the minimum number of coins needed

def f(amount_to_pay):
    coins = 0
    while amount_to_pay >= 5:
        amount_to_pay -= 5
        coins += 1
    while amount_to_pay >= 2:
        amount_to_pay -= 2
        coins += 1
    while amount_to_pay >= 1:
        amount_to_pay -= 1
        coins += 1
    return coins

if __name__ == "__main__":
    amount_to_pay = int(input("Enter the amount to pay: "))
    print(f"Number of coins needed: {f(amount_to_pay)}")