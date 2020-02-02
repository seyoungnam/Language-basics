def exception_test(value_1, value_2):
    print("계산을 시작합니다.")
    result = 0
    try:
        result = value_1 + value_2
    except:
        print("계산을 할 수 없습니다.")
    finally:
        print("계산을 종료합니다.")
    return result

if __name__ == '__main__':
    print(exception_test(100, 200))
    print(exception_test(100, "200"))