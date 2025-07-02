def add(*args):
    print(args[3])
    count = 0
    for n in args:
        count += n
    return count

a = add(2,3,4, 5,6,78,89,9 )
print(a)