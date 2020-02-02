def check_type(s):
    try:
        int(s)
        return 'integer'
    except ValueError:
        if type(s) == float():
            float(s)
            return 'float'
        else:
            return 'string'

if __name__ == '__main__':
    print(check_type('12'))
    print(check_type('1.23'))
    print(check_type('ab'))