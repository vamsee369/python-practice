class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        if self.length == self.width:
            print("it is a square")

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)


A = rectangle(10, 10)
print(A.area())
print(A.perimeter())
