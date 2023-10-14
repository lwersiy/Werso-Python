class Student:
    # Class Attribute
    school = "JJTech"

    def __init__(self, student_name, student_class, age):
        self.student_name = student_name
        self.student_class = student_class
        self.age = age

    def get_name(self):
        return self.student_name

    def get_school(self):
        return self.school

    def get_age(self):
        return self.age

    def get_class(self):
        return self.student_class


obj1=Student("Giddy", "Python", "16")
print(obj1.get_age())

obj2=Student("Showmik", "Terraform", "20")
print(obj2.get_school())

obj3=Student("Chimezie", "Ansible", "17")
