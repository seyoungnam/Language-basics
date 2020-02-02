# try~ exception~ else : try구문에서 exception 발생 않을 시 후속 작업 수행은 else문에서 처리
L = [1,2,3]
def func1():
    try:
        num = L[0]
    except IndexError:
        print('Index Error')
    else:
        print('Keep calm and go ahead')


if __name__ == '__main__':
    func1()