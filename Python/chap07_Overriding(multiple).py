class Dog:
    def sound(self):
        print("bark")

class Cat:
    def sound(self):
        print("meow")

class Chimera(Dog, Cat):
    pass

if __name__ == '__main__':
    Chimera().sound()   # 다중 상속 시 메소드 명이 동일할 경우 먼저 정의된 Dog의 sound()를 불러옴
    