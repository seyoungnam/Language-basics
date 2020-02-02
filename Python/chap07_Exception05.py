# 사용자 정의 Exception
class MyException(Exception):
    # 생성시 value값을 입력 받는다.
    def __init__(self, value):
        self.value = value

    # 생성시 받은 value값을 확인한다.
    def __str__(self):
        return self.value

# 예외를 발생하는 함수
def raise_exception(err_msg):
    raise MyException(err_msg) # 사용자 예외를 발생한다.
# Test
try:
    raise_exception("Error!! Error~!!!")
except MyException as e:
    print(e)