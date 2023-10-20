t=int(input())
di={}
while(t):
    t-=1
    x=input()
    if(x in di):
        di[x]+=1
    else:
        di[x]=1
for ky,vl in di.items():
    if(vl==1):
        print(ky)
        break
    
