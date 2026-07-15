class student:
    def __init__(self,id , name , marks):
        self.id = id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Id- {self.id}")
        print(f"Name- {self.name}")
        print(f"Marks- {self.marks}")
        print(f"Grade- {self.grade()}")


    def grade(self):
        if self.marks >= 90:
            result = 'A' 
        elif self.marks >=75:
            result = 'B' 
        else:
            result = 'C'
        return result


s = student(5,"Hitesh",99)
s.display()
s.grade()