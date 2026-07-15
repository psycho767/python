def even_no():
    for i in range(2,22,2):
        yield i
    
result = even_no()

for i in result:
    print(i)