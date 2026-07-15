class cus_iter:
    def __init__(self,no,inc,end_no):
        self.no = no
        self.inc = inc
        self.end_no = end_no
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if(self.no >= self.end_no):
            raise StopIteration
        else:
            result = self.no
            self.no += self.inc
            return result

no1 = input("Enter the Starting No-")
no2 = input("Enter the increment no-")
no3 = input("Enter the end no-")
s = cus_iter(int(no1),int(no2),int(no3))
for i in s:
    print(i)


