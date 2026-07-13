from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.__salary = salary

    @abstractmethod
    def work(self):
        pass

    def display(self):
        print(self.emp_id)
        print(self.name)

    def get_salary(self):
        return self.__salary


class Manager(Employee):

    def work(self):
        print("Managing Team")


class Developer(Employee):

    def work(self):
        print("Writing Code")


m = Manager(1, "Rahul", 50000)

d = Developer(2, "Aman", 60000)

m.display()
m.work()
print(m.get_salary())

print("----------------")

d.display()
d.work()
print(d.get_salary())