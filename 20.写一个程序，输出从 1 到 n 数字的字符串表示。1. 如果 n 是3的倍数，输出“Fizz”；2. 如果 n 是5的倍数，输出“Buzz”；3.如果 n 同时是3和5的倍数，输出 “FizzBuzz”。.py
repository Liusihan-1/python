n=int(input())
a_list=[]
for i in a_list(range(1,n+1)):
    if n%3==0:
        a_list.append("Fizz")
    elif n%5==0:
        a_list.append("Buzz")
    elif n%3==0 and n%5==0:
        a_list.append("FizzBuzz")
    else:
        a_list.append(int(n))
print(a_list)
