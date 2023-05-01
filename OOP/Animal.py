# Animal 클래스를 만들어서
class Animal:
    # 이름과 나이를 속성으로
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # speak를 메소드로 갖게
    def speak(self):
        print("The animal speaks")

# Dog클래스와 Cat 클래스를 각각 Animal 상속을 받아 만들어주게


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    # speak 메소드를 각각의 클래스에 맞게 구현

    def speak(self):
        print("멍멍")


# Dog클래스와 Cat 클래스를 각각 Animal 상속을 받아 만들어주게
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("야옹")


cute_dog = Dog("코기", "9")
cute_dog.speak()

cute_cat = Cat("나비", "7")
cute_cat.speak()
