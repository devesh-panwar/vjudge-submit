t=int(input())
while(t):
    t-=1
    n=int(input())
    swap=list(map(int,input().split()))
    
    b=set()
    max_el=0
    for x in range(n):
        if(swap[x] in b):
            b.remove(swap[x])
        else:
            b.add(swap[x])
        max_el=max(len(b),max_el)
    print(max_el)