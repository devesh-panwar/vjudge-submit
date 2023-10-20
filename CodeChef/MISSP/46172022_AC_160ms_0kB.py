t = int(input())
while(t):
    t-=1
    x=int(input())
    ls=[]
    for i in range(x):
        x-=1
        el=int(input())
        ls.append(el)
        
    di={}
    for i in ls:
        if(i in di):
            di[i]+=1
        
        else:
            di[i]=1
    for i in di:
        if(di[i]%2!=0):
            print(i)