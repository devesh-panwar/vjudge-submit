t=int(input())
while(t):
    t-=1
    x=int(input())
    ls=list(map(int,input().split()))
    
    st=set({})
    for i in (ls):
        st.add(i)
        
    print(len(st))