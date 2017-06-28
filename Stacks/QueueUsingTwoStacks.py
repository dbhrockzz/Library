class stack:
    
    def __init__(self):
        self.top = -1
        self.st = []
    
    def push(self,n):
        self.st.append(n)
        self.top+=1
    
    def pop(self):
        if self.top==-1:
            return
        self.top-=1
        return self.st.pop()
    
    def peek(self):
        return self.st[self.top]
    
    def isEmpty(self):
        if self.top==-1:
            return True
        return False
    
def main():
    stackA = stack()
    stackB = stack()
    while True:
        print "1. Enqueue"
        print "2. Dequeue"
        print "3. Exit"
        n = input("Choose an option : ")
        if n==1:
            num = input("Enter the number : ")
            stackA.push(num)
        if n==2:
            if stackA.isEmpty() and stackB.isEmpty():
                print "Queue is Empty"
            elif stackB.isEmpty():
                while not stackB.isEmpty():
                    stackB.push(stackA.pop())
                print "Deleted Element from Queue is",stackB.pop()
            else:
                print "Deleted Element from Queue is",stackB.pop()
        elif n==3:
            break
        else:
            print "Inavlid Input"
        print

if __name__=="__main__":
    main()            
