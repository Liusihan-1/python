n=int(input("请输入行数："))
l=[]
for i in range(n):
    l.append([])
    for j in range(n):
        l[i].append('')
for p in range(n):
    for q in range(p+1):
        if p==0 or q==0 or p==q:
            l[p][q]=1
        else:
            l[p][q]=l[p-1][q-1]+l[p-1][q]
for a in range(n):
    for b in range(a+1):
        print(l[a][b],end=' ')
    print('\n')
