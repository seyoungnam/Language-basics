# print(dir(__builtins__))  # builtin method list 확인
# print(dir(classmethod))   # class내 builtin method list 확인

class MYSU:
    def __init__(self,Su):
        self.Su = Su

    def __lt__(self, Su):
        print("self .Su < other.Su")
    
    def __gt__(self, Su):
        print("self .Su > other.Su")

    
if __name__ == '__main__':
    a = MYSU(100)
    b = MYSU(50)
    a>b
    a<b
