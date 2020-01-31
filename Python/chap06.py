# # 클래스 선언과 생성
# class Address:
#     def allPrn(self, name, addr, tel):
#         self.name = name
#         self.addr = addr
#         self.tel = tel
#         print(self.name, self.addr, self.tel)

# if __name__ == '__main__':
#     addr01 = Address()
#     addr01.allPrn("Dominica", "Seoul", "010-111-1111")
    
#     addr02 = Address()
#     addr02.allPrn("Dominico", "Busan", "010-222-2222")



# # __class__ 키워드와 private 멤버
# class Emp:
#     empno = 1
#     result = 0

# if __name__ == '__main__':
#     a1 = Emp()
#     a1.empno = "a111"
#     a1.result = 850

#     a2 = Emp()
#     a2.empno = "b111"
#     a2.result = 750

#     a3 = Emp()
#     a3.empno = "c111"
#     a3.result = 650

#     print("a1 empno : ", a1.empno, "| a1 result : ", a1.result)
#     print("a2 empno : ", a2.empno, "| a2 result : ", a2.result)
#     print("a3 empno : ", a3.empno, "| a3 result : ", a3.result)

#     print("a2.__class__.result : ", a2.__class__.result) #1을 출력, class 생성시에 부여된 변수 기초값 출력(line 18)
#     print("a3.__class__.result : ", a3.__class__.result) #1을 출력, class 생성시에 부여된 변수 기초값 출력(line 18)
#     print("Emp.result : ", Emp.result) #0을 출력, class 생성시 부여된 변수 기초값 출력
#     a1.__class__.result = 1000

#     print("a2.__class__.result : ", a2.__class__.result) # 1000 출력
#     print("a3.__class__.result : ", a3.__class__.result) # 1000 출력
#     print("Emp.result : ", Emp.result)   # 1000 출력

#     a4 = Emp()
#     print("a4.result : ", a4.result)    # 1000 출력

#     print(Emp.__class__)
#     print(Emp.__class__.__name__)
#     print(a1.__class__)
#     print(a1.__class__.__name__)


# Private 개념
class Test02:
    __b = 100 # private, Test02의 멤버에서만 접근이 가능
    def __m(self):
        return 'a'
    def k(self):
        print(self.__m(), self.__b) # self.__b 접근 가능

if __name__ == '__main__':
    y = Test02()
    y.k() # a 100
    print(y.__b) # 호출 불가

    