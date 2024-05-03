strx="Emma is good developer.Emma is good doog "
b=input()
cnt=0
for i in range(len(strx)):
    if i==b:
        cnt+=1
print(f"{b} apeared {cnt} times")

