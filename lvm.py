class st():
    def __init__(self):
        self.stack=[]
        self.register=0
        self.waitfor=-1
        
    def push(self,data):
        self.stack.append(data)
        
    def store(self):
        self.register=self.stack.pop()
    
    def load(self):
        self.stack.append(self.register)
        
    def plus(self):
        val=0
        for _ in range(2):
            val+=self.stack.pop()
        self.stack.append(val)
    
    def times(self):
        val=1
        for _ in range(2):
            val*=self.stack.pop()
        self.stack.append(val)
            
    def ifzero(self,n):
        if self.stack.pop()==0:
            return n
        else:
            return -1
    
    def done(self):
        print(self.stack[-1])

lvm=st()
n=int(input())
waitfor=-1

ins=[]
for _ in range(n):
    ins.append(list(input().split()))
    
i=0
while i<n:
    #print(f"{i+1}:",end='')
    if ins[i][0]=='PUSH':
        lvm.push(int(ins[i][1]))
    elif ins[i][0]=='STORE':
        lvm.store()
    elif ins[i][0]=='LOAD':
        lvm.load()
    elif ins[i][0]=='PLUS':
        lvm.plus()
    elif ins[i][0]=='TIMES':
        lvm.times()
    elif ins[i][0]=='IFZERO':
        waitfor=lvm.ifzero(int(ins[i][1]))
        if waitfor>0:
            i=waitfor-1
        #print(f"waitfor:{waitfor}",end=' ')
    elif ins[i][0]=='DONE':
        lvm.done()
        break
    #lvm.done()
    i+=1
    
