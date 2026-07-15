#Exception Handling

no1 = input("Please Enter the First no- ")
print(f"First no is - {no1}")
no2 = input("Please Enter the Second no- ")
print(f"Second no is - {no2}")

try:
    result = int(no1)/int(no2)
    print(result)
except Exception as ex:
    print(f"Exception is {ex}")
    print(f"Exception type is {type(ex)}")

