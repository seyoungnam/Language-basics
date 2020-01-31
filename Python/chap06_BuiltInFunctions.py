# Built-In Functions
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def aboutPerson(self):
        print("name : " + self.name + ", age : " + str(self.age))

    def __del__(self):
        print("call del")

if __name__ == '__main__':
    objectPerson = Person("Dominica", 20)
    objectPerson.aboutPerson()
    # ob = Person() # 에러 발생: constructor(__init__)내 parameter를 채우지 않았기 때문
    print(objectPerson)
    del objectPerson
    print(objectPerson) # 에러 발생: 이미 삭제한 인스턴스를 불렀기 때문
    