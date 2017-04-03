class queue:

    
    def __init__(self):
        self.q = []
        self.s = 0

    def enqueue(self,x):
        self.s+=1
        self.q.append(x)
    
    def dequeue(self):
        if self.s>0:
            self.s-=1
            return self.q.pop(0)
    
    def size(self):
        return self.s
    
    def isEmpty(self):
        return self.s==0

    def values(self):
        return self.q

