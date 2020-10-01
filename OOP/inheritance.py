
class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

def run():
    rectangle = Rectangle(length = 3, width = 5)
    print(rectangle.area())

    square = Square(side = 5)
    print(square.area())


if __name__ == "__main__":
    run()