//
li=list(input().strip())
start=0
for i in range(len(li)):
    if li[i] in "aeiou":
        for j in range(i,start-1,-1):
            if li[j] not in "aeiou":
                li[i]=li[j]
                start=j
                break
print(*li,sep="")
//
