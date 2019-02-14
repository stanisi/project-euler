'''Each new term in the Fibonacci sequence is generated by adding the previous 
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.'''

fiboseq = [1, 2]
ind = 0
SumEven = 0

while fiboseq[ind + 1] < 4000000:
    fiboseq.append(fiboseq[ind] + fiboseq[ind + 1])
    ind += 1

del fiboseq[-1]

for n in fiboseq:
    if (n%2 == 0):
        SumEven += n
        
print("Answer is:", SumEven)