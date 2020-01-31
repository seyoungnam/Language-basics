# 상속 유형은 크게 Sub classing과 Sub typing으로 나뉨
# Sub classing : 선조 클래스의 속성과 구조를 그대로 가지면서 새로운 데이터 멤버 변수와 멤버 메소드를 추가해서 코드 재사용
# Sub typing : 선조 클래스의 객체를 후손 클래스의 타입으로 대처하여 실행, abstract class와 duck typing을 지원
# ABCMeta : Abstract Base Classes Meta Class

from abc import abstractmethod, ABCMeta

class Base(metaclass=ABCMeta):  #추상 클래스로 선언되면 객체 생성 불가, 즉 x=Base() 불가
    @abstractmethod #추상 메소드
    def start(self):
        print("base start")

    @abstractmethod #추상 메소드
    def stop(self):
        print("base stop")

class Cat(Base):
    def start(self):
        print("cat start")

    def stop(self):
        print("cat stop")

class Duck(Base):
    def start(self):
        print("duck start")

    def stop(self):
        print("duck stop")

class Puppy(Base):
    def start(self):
        print("puppy start")

    def stop(self):
        print("puppy stop")

def MY_Call(m):
    m.start()
    m.stop()

if __name__ == '__main__':
    MY_Call(Puppy())
    MY_Call(Cat())
    MY_Call(Duck())
