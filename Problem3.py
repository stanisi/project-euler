'''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?'''

n = 600851475143
prime = 1
i = 2
while(i * i <= n):
    while(n % i == 0):
        prime = i
        n /= i
    i += 1
if (n > 1):
    prime = n
print(prime)