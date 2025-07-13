n,d=(map(int,input().split()))
j=list(map(int,input().split()))

j.sort(reverse=True)
jam=0
for i in range(d):
    jam+=j[i]
    
print(jam)
