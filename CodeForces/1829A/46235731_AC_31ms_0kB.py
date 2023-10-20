t=int(input())
while(t):
    t-=1
    st=input()
    ore='codeforces'
    c=0
    for i in range(len(st)):
        if(st[i]!=ore[i]):
            c+=1
    print(c)
    