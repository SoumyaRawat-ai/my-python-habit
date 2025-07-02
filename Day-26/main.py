with open("file1.txt") as file:
    a = [int(x.strip()) for x in file]
with open("file2.txt") as file:
    b = [int(x.strip()) for x in file]

result = [x for x in a if b  in a]
print(a)
print(b)
print(result)