number = [2,5,6,9,3,6]

no = iter(number)
num_len = len(number)
while num_len>= 1:
    print(next(no))
    num_len -=1