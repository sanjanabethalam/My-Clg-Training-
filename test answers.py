"""# Day 3 1st question"""

"""n = int(input())
if n<=0:
    print("Invalid Input")
else:
    arr=list(map(int,input().split()))
    k=int(input())
    if k>n:
        print("Invalid Input")
    else:
        fisrt = arr[:n-k]
        last = arr[n-k:]
        res = last+first
        print(*res)

#Day 3 2nd question"""

"""n = int(input())
arr = list(map(int,input().split()))
k = int(input())
res = []
for i in range(0, n-1):
    for j in range(i+1,n):
        if arr[i]*arr[j] == k:
            rs.append((arr[i], arr[j]))
print(res)"""

"""#Day4 1st question"""

n = int(input())
for i in range(n):
    action = input().split()
    if action[0] == "add":
        pass
    elif a[0] == "insert":
        pass
    elif a[0] == "remove":
        pass
    elif a[0] == "pop":
        pass
    elif a[0] == "print":
        pass


#Day 4 2nd question

n = int(input())
for i in range(n)):
    password = input()
    pass_len = len(password) >= 8 and len(password) <= 16
    alp = password[0].isalpha()
    upper = False
    lower = False
    digit = False
    special = False
    for i in password:
        if i.isdigit():
            digit = True
        elif i.isupper():
            upper = True
        elif i.islower():
            lower = True
        else:
            special = True
    if pass_len and alp and upper and lower and digit and special
        print
    





















    
