# Doit6-5.py
class MyList:
    def empty(self):
        self.data=[]
    def add(self, x):
        self.data.append(x)
    def getData(self):
        return list(self.data)

if __name__=='__main__':
    my01 = MyList() #my01이라는 객체 생성
    my01.empty()
    my01.add([x for x in range(1,6)]) # 1~5까지의 데이터를 목록으로 입력
    print(my01.getData()) # 저장된 데이터를 리턴받음
