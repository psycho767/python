# Create a generator that yields the cubes of numbers from 1 to 10.

def gen():
    for i in range(11):
        yield i**3
    
for i in gen():
    print(i)
