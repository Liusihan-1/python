def func_sum(a_list):
    s=0
    for i in range(0,len(a_list)):
        if a_list[i]%2==0:
            s=s+a_list[i]
    return s
#exp8.12.py
import evensum
a_list=[3,54,65,76,45,34,100,-2]
s=evensum.func_sum(a_list)
print("sum=",s)

























