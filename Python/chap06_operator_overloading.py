# Operator Overloading
# https://blog.hexabrain.net/287

class Num:
    def __init__(self, num):
        self.num = num
    def __add__(self, num):
        self.num += num
    def __sub__(self, num):
        self.num -= num

if __name__ == '__main__':
    n=Num(100)
    print(n.num) # 100을 출력
    n+100
    print(n.num) # 200을 출력, def __add__ 지정해주지 않으면 에러 발생, n+100은 n.__add__(100)을 호출하는 것과 동일
    n-100
    print(n.num) # 300을 출력, def __sub__ 지정해주지 않으면 에러 발생


