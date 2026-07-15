class Student:

    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name

    def display(self):
        print(self.name)

s1 = Student("Rahul")
s2 = Student("Aman")

s1.change_name("Rohit")

s1.display()
s2.display()