from random import randrange    # random의 모듈을 import

def loto(): # 로또 함수를 선언
    numeros = list(range(1,50))
    resultat = []
    for i in range(5):
        rnd = randrange(50 - i)
        resultat.append(numeros[rnd])
        numeros[rnd] = numeros[-1]
    # 마지막 자릿수는 1~10까지의 숫자로만 저장한다.
    resultat.append(randrange(10) + 1)
return resultat

if __name__ == '__main__':
    print(loto())