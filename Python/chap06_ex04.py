# Doit6-4.py
import re
list1 = [1,2,3,4,5]

def three_times(x):
    return x*3

def my_split(word):
    return re.split("[0-9]",word)

def my_join(strs):
    print(" @".join(strs))
    print(":".join(strs))

if __name__ == '__main__':
    print(list(map(three_times, list1)))
    print(list(map(three_times, ["ha", "ho"])))
    print(list(map(lambda x : x*3, list1)))

    print(my_split('ab7cde7abd5abc')) #숫자를 기준으로 split

    strs = ["Hello", "Dominica", "and", "RuSe"]
    my_join(strs)