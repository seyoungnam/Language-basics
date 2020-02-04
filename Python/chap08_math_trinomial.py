from math import sqrt

def Trinomial(a, b, c):
    delta = b**2 - 4*a*c # b2 - 4ac
    # if delta>0 => 근의 공식 이용
    if delta > 0.0:
        racine_delta = sqrt(delta)
        return (2, (-b-racine_delta)/(2*a), (-b+racine_delta)/(2*a))
    elif delta < 0.0:
        return (0,)
    else: # 0과 같을 경우 x1 = x2 = -b/(2a)의 공식으로 리턴
        return (1, (-b/(2*a)))

if __name__ == '__main__':
    print(Trinomial(1.0, -3.0, 2.0))
    print(Trinomial(1.0, -2.0, 1.0))
    print(Trinomial(1.0, 1.0, 1.0))