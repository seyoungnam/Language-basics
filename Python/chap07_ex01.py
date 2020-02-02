class List2(list):
    def get(self, i, default=None):
        if not isinstance(i, int):
            raise KeyError('index must be integer')
        elif i < 0 :
            raise KeyError('index out of range')

        if i >= len(self):
            return default
        else:
            return self[i]

if __name__ == '__main__':
    Res = List2(range(10))
    print(Res)
    print(Res.get(0.2,None))
    print(Res.get(-1, None))