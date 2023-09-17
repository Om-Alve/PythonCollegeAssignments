n=5
rows = (n*2)-1
cols = (rows*2)-1
indexes = [cols//2]
mid = cols//2

for i in range(1,n+1):
    ch = ord('a') + n-1
    for j in range(cols):
        if j in indexes:
            print(chr(ch),end=" ")
            if j>=mid:
                ch+=1
            else:
                ch-=1
        else:
            print("-",end=" ")
    print("")
    indexes.append(mid+i*2)
    indexes.append(mid-i*2)

indexes.pop()
indexes.pop()
        
for i in range(1,rows-n+1):
    indexes.pop()
    indexes.pop()
    ch = ord('a') + n-1
    for j in range(cols):
        if j in indexes:
            print(chr(ch),end=" ")
            if j >= mid:
                ch+=1
            else:
                ch-=1
        else:
            print("-",end=" ")
    print("")


