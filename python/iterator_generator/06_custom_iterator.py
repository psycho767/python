class gen:
    def __init__(self):
        self.current = 100;

    def __iter__(self):
        return self

    def __next__(self):
        if(self.current <= 500):
            value = self.current
            self.current +=100
            return value
        else:
            raise StopIteration

s = gen()
for i in s:
    print(i)
