with open("/Users/soumy/OneDrive/Cloud storage/OneDrive/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("C:/Users/soumy/OneDrive/Cloud storage/OneDrive/Desktop/my_file.txt", 'w') as file:
    file.write('hello')

# "C:\Users\soumy\PycharmProjects\day-24\new_file.txt"
with open("../new_file.txt") as file:
    a = file.read()
    print(a)