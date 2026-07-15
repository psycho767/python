students = [
    ("Aman", 80),
    ("Riya", 95),
    ("Raj", 70)
]

#print(students[0][0])

result =list(map(lambda x:x[0],students))
print(result)

result =list(map(lambda x:x[1],students))
print(result)

result =list(map(lambda x: x[0] + " Scored " + str(x[1]) ,students))
print(result)

result = list(map(lambda X: (X[0] ,X[1]+5 ) ,students))
print (result)

result = dict(students)
print (result)