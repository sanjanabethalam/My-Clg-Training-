"""def prime(num):
    count = 0
    for i in range(1, num+1):
        if num%i ==0:
            count += 1
    if count == 2:
        print("prime")
    else:
        print("not prime")
prime(6)"""


def add(a,b, *abc):
    print(a)
    print(b)
    print(abc)
print(add(10,20,30,40,50))


def func(n):
    print(n)
    if n>0:
        check(n-1)
        check(5)
print(5)

""" #Type of Functions

1. Regular functions
2. Default functions # instead of taking error it takes default value
3. Keyword argument functions # While calling to function it gives values to the argument 
4. variable length functions # it take any no.of variables"""
