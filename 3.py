#一个整数
#它加上100后是一个完全平方数
#再加上168又是一个完全平方数
#请问该数是多少
import math
for i in range(-100,1000):
   a=math.sqrt(i+100)
   b=math.sqrt(i+268)
   if int(a)==a and int(b)==b:
        print(i)
