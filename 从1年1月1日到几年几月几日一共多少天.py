def LeapYear(y):
    if y<1:
        y=1
    if ((y%400)==0 or (y%4)==0 and (y%100)!=0):
        lp=1
    else:
        lp=0
    return lp
def getLastDay(y,m):
    if y<1:
        y=1
    if m<1:
        m=1
    if m>12:
        m=12
    monthDay=[31,28,31,30,31,30,31,31,30,31,30,31]
    r=monthDay[m-1]
    if m==2:
        r=r+LeapYear(y)
    return r
def calcDays(y,m,d):
    if y<1:
        y=1
    if m<1:
        m=1
    if m>12:
        m=12
    if d<1:
        d=1
    if d>getLastDay(y,m):
        d=getLastDay(y,m)
    T=0
    for i in range(1,y):
        T=T+365+LeapYear(i)
    for i in range(1,m):
        T=T+getLastDay(y,i)
    T=T+d
    return T
y,m,d=eval(input("input year,month,day:"))
days=calcDays(y,m,d)
print("从1年1月1日到",y,"年",m,"月",d,"日共",days,"天")
        
        
