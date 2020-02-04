from random import *
from decimal import *

print(random()) # 0.0 ~ 1.0 사이의 float값을 return
print(uniform(1,100))   # 1~100 사이 임의의 float값 return
print(randint(1,100))   # 1~100 사이의 int값을 return
print(choice("1234567890abcdefghij"))   # "" 내에서 하나의 요소를 return

sample_list = ["python", "java", "c++", "random", "spring"]
shuffle(sample_list)
print(sample_list)