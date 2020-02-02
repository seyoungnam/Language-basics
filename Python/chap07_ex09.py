class MyException(Exception):
    def __init__(self, message):
        self.message = message

try:
    num1, num2 = eval(input("input num1,num2: "))
    if num2==0:
        raise MyException("0으로 나누려 했음")
    reslut = num1 / num2
    print("Result is ", result)
except MyException as e:
    print(e.message)
