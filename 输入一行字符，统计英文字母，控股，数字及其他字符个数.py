a_list=list(input('请输入一行字符:'))
letter=[]
space=[]
number=[]
other=[]

for i in range(len(a_list)):
    if ord(a_list[i]) in range (65,91) or ord(a_list[i]) in range(97,123):
        letter.append(a_list[i])
    elif a_list[i]==' ':
        space.append(' ')
    elif ord(a_list[i]) in range(48,58):
        number.append(a_list[i])
    else:
        other.append(a_list[i])

print('英文字母个数: %s' %len(letter))
print('空格个数: %s' %len(space))
print('数字个数: %s' %len(number))
print('其他字符个数: %s' %len(other))

