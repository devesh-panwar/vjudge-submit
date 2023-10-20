t=int(input())

while(t):
    t-=1
    x=int(input())
    ls=[]
    for y in range(1,x+1):
        if(x%y==0):
            ls.append(y)
            
    ev=0
    odd=0
    for y in ls:
        if(y%2==0):
            ev+=1
        else:
            odd+=1
            
    if(ev>odd):
        print(0)
    elif(ev==odd):
        print(1)
    else:
        print(0)