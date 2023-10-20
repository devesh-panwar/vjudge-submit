t=int(input())
while(t):
    t-=1
    st=input()
    if(len(st)>10):
        print(st[0]+str(len(st)-2)+st[len(st)-1])
    else:
        print(st)