class My:
    def __init__(self):
        self.x=0

    @property # getter에 해당
    def mFun(self):
        return self.x

    @mFun.setter # setter에 해당
    def mFun(self, x):
        self.x = x

    @classmethod # 상속시 cls인자를 활용하여 자손클래스의 속성을 가져옴
    def class_Fun(cls,x):
        print("class_Fun(%s%d)"%(cls,x))

    @staticmethod # 상속시 부모클래스의 속성값을 가져옴
    def static_Fun(x):
        print("static_Fun(%d)"%x)

if __name__ == '__main__':
    a=My()
    a.mFun=int(100)
    print(a.mFun)

    My.class_Fun(10)
    My.static_Fun(10)

