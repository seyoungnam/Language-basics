class Person:   # Base class
    def __init__(self, name, age): # 이름과 나이를 입력 받아 초기화
        self.name = name
        self.age = age

    def PersonInfo(self): # 이름과 나이를 출력하는 메소드
        return self.name + " : (age :" + str(self.age) + ")"

class Student(Person):
    def __init__(self, name, age, grade):
        Person.__init__(self, name, age) # 선조의 생성자를 호출해서 값 전달, super().__init__(name, age)
        self.grade = grade
    
    def GetStudent(self):
        return self.PersonInfo() + ", grade : " + str(self.grade) # self.PersonInfo() == super().PersonInfo()

if __name__ == '__main__':
    x = Person("Dominica", 12)
    y = Student("Ruri", 7, 3)

    print(x.PersonInfo())
    print(y.PersonInfo())
    print(y.GetStudent())