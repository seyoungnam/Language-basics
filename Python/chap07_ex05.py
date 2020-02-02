def mydecolater(func):
    def wrapper():
        print("start")
        func()  # @데코레이션이 실행될 대상 함수를 실행
        print("end")
    return wrapper

@mydecolater # mydecolater 내 func()을 채워줌
def MTest():
    print("MTest exec")

if __name__ == '__main__':
    MTest() # => start, MTest exec, end