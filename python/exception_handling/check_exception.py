try:
    a = 10
    b = 0
    print(a / b)

except Exception as ex:
    print(f"Exception is {ex}")
    print(f"Exception type is {type(ex)}")