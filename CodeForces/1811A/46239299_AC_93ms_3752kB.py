
t = int(input())
results = []

for _ in range(t):
    n, d = map(int, input().split())
    number = input()
    
    result = list(number)
    
    for i in range(n):
        if int(number[i]) < d:
            result.insert(i,str(d))
            break
    else:
        result.append(str(d))
        
    results.append("".join(result))


for result in results:
    print(result)
