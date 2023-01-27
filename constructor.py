"""Constructor are also called as initializers(__init__) in python"""




class student:
    student_name="no name"
    def __init__(self, name):
       self.student_name=name
    def update_name(self, new_name):
        pass
s1 = student("sanjana")
s2 = student("swathi")
s3 = student("bala")
print(s1.student_name)



class student:
    student_name="no name"
    def __init__(self, name):
       self.student_name=name
    def update_name(self, new_name):
        pass
s1 = student("sanjana")
s2 = student("swathi")
s3 = student("bala")
print(s1.student_name)
