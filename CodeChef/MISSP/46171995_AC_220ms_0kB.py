
T = int(input())


for _ in range(T):
   
    N = int(input())
    
    
    doll_count = {}
    
    
    for _ in range(N):
        doll = int(input())
        if doll in doll_count:
            doll_count[doll] += 1
        else:
            doll_count[doll] = 1
    
    
    for doll_type, count in doll_count.items():
        if count % 2 != 0:
            print(doll_type)
            break
