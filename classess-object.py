class Student:
    school = "jjtech"

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

giddy = Student("giddy", "Python", "19")
print(giddy.get_age())

showmik=Student("Showmik", "Terraform", "28")
print(showmik.get_school())

Chimezie=Student("Chimezie", "Ansible", "16")
print(Chimezie.get_class())


