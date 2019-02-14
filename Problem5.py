'''2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?'''

list1 = []
sn = 1

while len(list1) == 0:
    remainder = 0.0
    for n in range(1, 21):
        remainder += sn%n
        if(remainder > 0):
            break
    if(remainder == 0):
        list1.append(sn)
    sn += 1
    
# Answer is 232792560