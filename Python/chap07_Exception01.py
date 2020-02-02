# 에러 메세지 확인
try:
    10/0
except ZeroDivisionError as e:
    print(e)

# 예외 발생시 정보를 보유하고 있는 메소드 활용
try:
    10/0
except ZeroDivisionError as e:
    print(format(type(e))) # 매우 중요! => exception class 찾을 때 사용
    print(format(e.args))
    print(format(e))

