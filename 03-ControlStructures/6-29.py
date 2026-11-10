####
# A natural number greater than 1 is called a prime 
# if it has exactly 2 natural factors with the values 
# 1 and this number. Write a program that finds N leading 
# prime numbers. Read the value of N from the keyboard. 
# Using loop statements check that the number N is divisible 
# only by 1 and by N.

n = 11
if n <= 1:
    print(False)
else:
    prime = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break
    print(prime)