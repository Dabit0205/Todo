# Shape 클래스를 만들어서
class Shape:
    def __init__(self, name):
        self.name = name

    # get_area메소드를 갖게 해주세요.
    def get_area(self):
        return self.area

# Circle과 Rectangle 클래스를 Shape를 상속받아 만들어주세요


class Circle(Shape):

    # Circle은 radius 속성을 가지게
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    # get_area메소드는 각각에 맞게 구현
    def get_area(self):
        self.area = self.radius * self.radius * 3.14
        print(self.area)

# Circle과 Rectangle 클래스를 Shape를 상속받아 만들어주세요


class Rectangle(Shape):

    # Rectangle은 length와 widht 속성을 가지게
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    # get_area메소드는 각각에 맞게 구현
    def get_area(self):
        self.area = self.width * self.length
        print(self.area)


myCircle = Circle("원", 8)
myCircle.get_area()

myRectangle = Rectangle("사각형", 5, 6)
myRectangle.get_area()
