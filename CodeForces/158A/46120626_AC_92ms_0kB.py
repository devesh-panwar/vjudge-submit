n, k = map(int, input().split())
scores = list(map(int, input().split()))

advancers = 0
for i in range(n):
    if scores[i] >= scores[k-1] and scores[i] > 0:
        advancers += 1
    else:
        break

print(advancers)