class Animal():
    def __init__(self):
        self.no_of_eyes = 2
    def breathe(self):
        print("inhale exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.fine = 2
    def swim(self):
        print("underwater")
    def breathe(self):
        super().breathe()
        print("breathe under water")


Nemo = Fish()
print(Nemo.fine, Nemo.no_of_eyes)
Nemo.swim()
Nemo.breathe()
