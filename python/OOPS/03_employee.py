class employee:
    def __init__(self,id,name,annual_salary):
        self.id = id
        self.name = name
        self.annual_salary = annual_salary
    def display_details(self):
        print(f"ID-{self.id}")
        print(f"Name-{self.name}")

    def display_salary(self):
        print(f"Salary-{self.annual_salary}")

emp_det = employee(1,"hitesh",50000)


emp_det.display_details()
emp_det.display_salary()

