a=input()
n=[]
for i in range(len(a)):
    if a[i]!=a[i-1]:
        n.append(a[i])
print("".join(n))


