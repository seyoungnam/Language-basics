class MyClassA(object):
    def __init__(self):
        self.val1 = 123

class MyClassB(MyClassA):
    def __init__(self):
        super().__init__()
        self.val2 = 456

if __name__ == '__main__':
    a=MyClassB()
    print(a.val1)
    print(a.val2)