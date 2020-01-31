class Mstack:
    def __init__(self): # 생성자 작성
        self.stack = []
        print("Hi Mstack")

    def push(self, str1):
        self.stack.append(str1)
        print(self.stack, type(str1), str1) # 목록과 타입 및 입력된 데이터 출력

    def pop(self):
        return self.stack.pop()

    def length(self):
        return len(self.stack)  # self.stack의 길이를 리턴

    def __del__(self):
        print(" bye Mstack")

if __name__ == '__main__':
    a1 = Mstack()
    for x in range(1,6):
        a1.push(x)
    a1.pop()
    print("length :", a1.length())
