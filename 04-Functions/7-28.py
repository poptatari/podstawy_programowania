# This function finds the most frequently rolled die 
# in a sequence of dice rolls.

def f(dice):
    rolled_most = dice[0]
    for i in dice:
        if dice.count(i) > dice.count(rolled_most):
            rolled_most = i
    return rolled_most

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))