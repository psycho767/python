#Each employee gets a 10% salary increase.

employees = [
    ("Rahul", 50000),
    ("Aman", 70000),
    ("Riya", 60000)
]

result = list(map(lambda x:(x[0],x[1]+(x[1]*10/100)) , employees))
print(result)

output:
[('Rahul', 55000.0), ('Aman', 77000.0), ('Riya', 66000.0)]