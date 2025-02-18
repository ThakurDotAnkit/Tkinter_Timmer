def add(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum

print(add(10,10,10,10,10))