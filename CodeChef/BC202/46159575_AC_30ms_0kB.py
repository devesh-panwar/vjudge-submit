t=int(input())

while(t):
    t-=1
    x=int(input())
    
    ls=list(map(int,input().split()))
    
    di={}
    for x in ls:
        if(x in di):
            di[x]+=1
        else:
            di[x]=1
    
    for x in di:
        print(x,end=" ")
            
    print()