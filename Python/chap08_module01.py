# 이 파일이 저장된 폴더에서 python shell을 열어 import chap08_module01 as my로 부르면
# print(my.pi)이나 print(my.area(5)) 등과 같이 호출 가능

pi = 3.14159
_b = 100
def area(r):
    return(pi*r*r)

def callB():
    print(_b)