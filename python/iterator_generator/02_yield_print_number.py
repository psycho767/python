def number():
    for i in range(10):
        yield i;


result = number()

for i in result:
    print(i)