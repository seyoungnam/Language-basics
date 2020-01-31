# 다형성(Polymorphism) : 어떤 한 요소에 여러 개념을 넣어 놓는 것
# 일반적으로 Overriding과 Overloading을 의미
# Overriding : 같은 이름의 메소드가 여러 클래스에서 다른 기능을 하는 것
# Overloading : 같은 이름의 메소드가 인자의 개수나 자료형에 따라서 다른 기능을 하는 것

def m_f(x,y):
    print("values: ", x, y)

if __name__ == '__main__':
    m_f(42, 43)
    m_f(42, 43.7)
    m_f(42.3, 43)
    m_f(42.0, 43.9)

