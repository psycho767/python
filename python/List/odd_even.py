numbers = [1, 2, 3, 4, 5, 6]
print("Even No - ")
print([x for x in numbers if x%2==0])
print("Odd No-")
print([x for x in numbers if x%2 !=0])

print("Result")
print(["Pass" if x > 3  else "fail" for x in numbers ])