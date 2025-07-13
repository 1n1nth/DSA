n=int(input())
day=list(map(int,input().split()))
night=list(map(int,input().split()))
limit=int(input())

day.sort(reverse=True)
night.sort()

overpay=0

for i in range(len(day)):
    total=day[i]+night[i]
    if total>limit:
        overpay+=total-limit
        
print(overpay*100)
