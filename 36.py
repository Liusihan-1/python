#36.请输入星期几的第一个字母来判断一下是星期几，
#如果第一个字母一样，
#则继续判断第二个字母。
letter = input('请输入首字母（大写）：')
if letter == 'S':
    letter = input('请输入第二个字母（小写）：')
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('输入错误！')
elif letter == 'M':
    print('Monday')
elif letter == 'T':
    letter = input('请输入第二个字母（小写）：')
    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('输入错误！')
elif letter == 'W':
    print('Wednesday')
elif letter == 'F':
    print('Friday')
else:
    print('输入错误！')
