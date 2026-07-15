def alphabet():
    yield 'A'
    yield 'B'
    yield   'C'
    yield   'D'

result = alphabet();
print(next(result))
print(next(result))
print(next(result))
print(next(result))
