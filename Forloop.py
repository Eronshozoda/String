n=int(input())
for j in range(1, n+1):
    print("* " * j)
    
for i in range(n + 1, 0, -1):
    
    for j in range(0, i - 1):
    
        print("*", end=' ')
    print(" ")
    