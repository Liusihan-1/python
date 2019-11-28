x,y,z=eval(input("请输入三个数字"))
if x>y:
      x,y=y,x
if x>z:
      x,z=z,x
if y>z:
      y,z=z,y
print(x,y,z)
           
