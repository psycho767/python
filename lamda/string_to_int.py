numbers = ["100", "200", "300", "400s"]

result = list(map(lambda x: int(x) if x.isdigit() else x,numbers))
print(result)