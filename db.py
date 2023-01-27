db = [
    {'abc@example.com': 'abc'},
    {'xyz@example.com': '123'},
    {'a123@example.com': 'qwertyuiop'},
    {'zxcv@example.com': '1234567890'}
    ]
for i in range(2):
 print(db)
username = input("enter username:")
password = input("enter username:")
temp = {username: password}
if temp in db:
    print("found")

