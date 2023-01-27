""""#inheritance
1.Single inheritance # one parent class one child class
2.Multilevel inheritance # one parent class multiple child class by levels
3.Hierarchical inheritance # one parent class multiple child class
4.Multiple inheritance # multiple parent class one child class

Example:"""
class A:
    name = "Mukesh"
    age = 36
class B(A):
    age = 10
obj = B()
obj.name = "Ramesh"
print(obj.age)
print(obj.name)

"""3.Example
class Person:
    name="Lakshmi"
    gender="female"
    age="60"
    pass
class Patient(person):
    disease="Fever"
    bloodgroup="A+"
    temperature="97"
class Doctor(person):
    def



4.Example"""
class p1:
    def m1 (self):
        print("in parent class 1")
class p2:
    def m1 (self):
        print("in parent class 2")
class c(p2, p1):
    pass
obj=c()
obj.m1()


    
