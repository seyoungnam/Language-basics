# Overriding : 상속받은 후손 클래스에서 상속해 준 선조 클래스에 이미 정의되어 있는 메소드의 기능을 변경해서 새로 정의하는 것
class MyScore:
    def __init__(self,kor,eng):
        self.kor=kor
        self.eng=eng

    def getTot(self):
        return (self.kor+self.eng)

class MyScore_Sub(MyScore):
    def __init__(self,kor,eng,mat):
        super().__init__(kor,eng)
        self.mat=mat

    def getTot(self):   # Override
        return (str(super().getTot()+self.mat))


if __name__ == '__main__':
    print(MyScore(57,67).getTot())
    print(MyScore_Sub(100,100,100).getTot())