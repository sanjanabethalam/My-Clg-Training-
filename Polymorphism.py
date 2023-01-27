"""class A:
    def method_1(self,a,b):
        print("sum of 2 numbers:",a+b)
class B(A):
    def method_1(self, abc):
        print("value is ", abc)
    def method_1(self, a,b):
        print("mul of 2 numbers:",a*b)
ob = B()
ob.method_1(10 ,20)



def invert(string):
    res = ""
    for i in string:
        if i == '0':
            res += '1'
        else:
            res += '0'
    return res
a = 5
b = 7
op = 'A'
new_a = bin(a)[2:]
new_b = bin(b)[2:]
new_a = invert(new_a)
new_b = invert(new_b)
print(new_a, new_b)
x = int(new_a,2)
y = int(new_b,2)

#method overridding(same method different class)
class A:
    def m1(self):
        print("in class A")
class B:
    def m1(self):
        print("in class B")
obj()

#Example"""
class animal:
    def eat(self):
        pass
    def sound(self):
        print('sound')
    def dog(animal):
        print('dog barks')
        pass
    def cat(animal):
        print('cat meow')
        pass
    def lion(animal):
        print('lion roars')
obj=animal()
obj.cat()