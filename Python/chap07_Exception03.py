# try~ exception(2가지 이상 경우)~ finally
try:
    print('try- 시작')
    a = int('고의 에러구문') # 예외발생
    print('try- 종료')
except (ZeroDivisionError, IOError, ValueError):
    print('0으로 나눴거나 파일이 존재하지 않음.')
else:
    print('else 도착')
finally:
    print('finally 도착')