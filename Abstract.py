"""from abc import ABC, abstractmethod
class Area(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Square(Area):
    def calculate_area(self):
        print("in Square method")

class Reactangle(Area):
    pass
ob=Square()
ob.calculate_area()

#Example"""
from abc import ABC,abstractmethod
class worker(ABC):
    @abstractmethod
    def serve(self):
        pass
    def cleaning(self):
        pass
class worker1(worker):
    def serve(self):
        print("worker1 serves biriyani")
    def cleaning(self):
        print("worker1 cleans tables")
class worker2(worker):
    def serve(self):
        print("worker2 serves fried rice")
    def cleaning(self):
        print("worker2 cleans plates")
class worker3(worker):
    def serve(self):
        print("worker3 serves white rice")
    def cleans(self):
        pass
ob=worker1()
ob.serve()
ob.cleaning()

