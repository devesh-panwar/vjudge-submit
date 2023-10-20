n=int(input())
st=n
di={}
while(n):
    n-=1
    x,y=map(str,input().split())
    di[x]=y
n=st  
while(True):
    try:
        
        
        x=input()
        if(x in di):
            print(x+"="+di[x])
        else:
            print('Not found')
            
    except EOFError:
        
        break
    