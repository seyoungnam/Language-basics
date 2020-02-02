import sys
import traceback
def my_test(value_1, value_2):
    print("계산을 시작합니다.")
    result = 0
    try:
        result = value_1 + value_2
    except:
        print("타입 에러로 계산을 할 수 없습니다.")
        raise
    finally:
        print("계산을 종료합니다.")
    return result

def calc(list_1,list_2):
    try:
        print(my_test(list_1[0], list_2[0])) #100+100
        print(my_test(list_1[1], list_2[1])) #200+200
        print(my_test(list_1[2], list_2[2])) #300+"300"
    except:
        #print("오류가 발생했습니다.")
        print(traceback.format_exc(sys.exc_info()[2]))

if __name__ == '__main__':
    list_1 = [100,200,300]
    list_2 = [100,200,"300"]
    calc(list_1,list_2)