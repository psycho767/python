def table():
    for i in range(1,11):
        yield i*7

result = table()

for i in result:
    print(i)