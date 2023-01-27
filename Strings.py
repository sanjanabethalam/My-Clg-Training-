"""s1 = "hello@world"
s2 = "HI THERE"
print(s1.upper())
print(s2.lower())"""

     #String formatting

"""first = "mr.x is"
age=38
last="years old"
print("Mr x is {} years old".format(age))
print("Mr x is {} years ols now and {} ".format(age,age*age))"""

    #Exception handlind

"""a=int(input())
b=int(input())
print(a+b)
print(a-b)
print(a*b)
try:
    print(a/b)
    print(a//b)
except:
    print("b cannot be 0")
    print("error handling")"""


a=int(input("enter a number:"))
b=int(input("enter a number:"))
op=input()
if op=="+":
    print(a+b)
if op=="-":
    print(a-b)
if op=="*":
    print(a*b)
try:
    if op=="/":
     print(a/b)
    if op=="//":
     print(a//b)
    if op=="%":
     print(a%b)
except:
    print("b cannot be zero")
if op=="<":
    print(a<b)
if op==">":
    print(a>b)
    
    
