# 자동차 클래스를 만들어주세요
# 모델, 색, 현재 속도를 속성을 갖고
# 속도를 올려주는 accelerate 메소드
# 속도를 낮춰주는 brake 메소드
# 현재 속도를 리턴해주는 get_speed 메소드를 추가


class Car:
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


my_car = Car("아반테", "회색")

print(my_car.color)

my_car.accelerate()
my_car.accelerate()
my_car.accelerate()
my_car.brake()
my_speed = my_car.get_speed()
print(my_speed)
