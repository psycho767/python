def difference():
    yield 5
    yield 10
    yield 15
    yield 20
    yield 25

result = difference();
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))