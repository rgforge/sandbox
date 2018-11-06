#! /usr/bin/python
def fibotest(n):
    if n <= 1:
        return(n)
    else:
        return(fibotest(n-1) + fibotest(n-2))


nterms1 = int(input('What is your first integer?   '))
nterms2 = int(input('What is your second integer?   '))
fibo1 = []
fibo2 = []

if nterms1 <= 0:
    print("Must be a positive integer")
else:
    for i in range(nterms1):
        fibo1.append(fibotest(i))

if nterms2 <= 0:
    print("Must be a positive integer")
else:
    for i in range(nterms2):
        fibo2.append(fibotest(i))


largest1 = (max(fibo1))
largest2 = (max(fibo2))

print(max(largest1, largest2))
