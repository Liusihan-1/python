#13.古典问题：有一对兔子
#从出生后第3个月起每个月都生一对兔子
#小兔子长到第三个月后每个月又生一对兔子
#假如兔子都不死，问每个月的兔子总数为多少
month=int(input("繁殖几个月："))
month_1=1
month_2=0
month_3=0
month_adult=0
for i in range(month):
    month_1,month_2,month_3,month_adult=month_adult+month_3,month_1,month_2,month_adult+month_3
    print("第{}个月共{}对兔子".format(i+1,month_1+month_2+month_3+month_adult))
    print("其中一月兔:",month_1)
    print("其中二月兔:",month_2)
    print("其中三月兔:",month_3)
    print("其中成年兔:",month_adult)
    
