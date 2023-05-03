# 2023.04.28, 객체지향 특강

class Car:
    color = 'red'

    def __init__(self, model, manufacterer, color, top_speed):
        self.model = model
        self.manufacterer = manufacterer
        self.color = color
        self.top_speed = top_speed
        self.speed = 0

    def accelerate(self, amount):
        self.speed += amount
        if self.speed > self.top_speed:
            self.speed = self.top_speed

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def drive(self):
        print("부릉부릉")

    def get_speed(self):
        return self.speed


print(Car.color)


class Car1:
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self):
        self.speed += 10

    def brake(self):
        self.speed -= 10

    def get_speed(self):
        return self.speed
    
    def set_speed(self, value):
        self.speed = value
        


car = Car1("소나타", "빨간색")
car.get_speed()
car.set_speed(100)

