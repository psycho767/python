class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee : {self.name}")

class Manager(Employee):

    def manage(self):
        print("Managing Team")


m = Manager("Rahul")

m.display()
m.manage()