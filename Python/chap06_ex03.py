def test(x,y,z):
    print(x,y,z)

def test01(**args):
    print(args)

def test02(a,b,c,d):
    print(a,b,c,d)

if __name__=='__main__':
    p = (10,20,30)
    test(*p)
    test(p[0],p[1],p[2])

    test01(ko="korea", en="English", fr="french")
    d = {'a': 'append', 'b': 'block', 'c': 'circle', 'd': 'date'}
    test02(**d)