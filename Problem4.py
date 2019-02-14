'''A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''


palilist = []
for n in range(100, 999):
    for m in range(100, 999):
        if (str(m*n) == str(m*n)[::-1]):
            palilist.append(m*n)
palilist.sort(reverse = True)
print("Answer :", palilist[0])