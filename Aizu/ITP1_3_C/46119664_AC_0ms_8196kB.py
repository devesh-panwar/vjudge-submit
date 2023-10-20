while True:
    x, y = map(int, input().split())  # Read two integers x and y

    if x == 0 and y == 0:
        break  

   
    print(min(x, y), max(x, y))