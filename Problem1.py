'''If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

n = int(input("Input a natural number ").strip())
total = 0

for m in range(1, n):
    if(m%3 == 0 or m%5 == 0):
        total += m
#        print("Running total (+", m, "): ", total)
        
print("Sum of natural numbers that are multiples of 3 or 5 below", n, "is:", total)