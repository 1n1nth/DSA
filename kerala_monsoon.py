n=int(input())
buildings=[]
for _ in range(n):
    building=list(map(int,input().split()))
    buildings.append(building)
    

protected_range=[]

for x,y in buildings:
    left=x-y
    right=x+y
    protected_range.append((left,right))
    
protected_range.sort(key=lambda x:x[1])
count=0
range=float("-inf")
for left,right in protected_range:
    if left>range:
        count+=1
        range=right
        
print(count)

    
