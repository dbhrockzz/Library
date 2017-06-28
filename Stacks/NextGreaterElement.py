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
    arr = map(int, raw_input("Enter the space separated array : ").strip().split())
    n = len(arr)
    st = stack()
    nge = [-1]*n
    for i in range(n):
        next = arr[i]
        if st.isEmpty():
            st.push(i)
        else:
            while not st.isEmpty() and arr[st.peek()] < next:
                temp = st.pop()
                nge[temp] = next
            st.push(i)
    for i in range(n):
        print arr[i],"-->",nge[i]

if __name__=="__main__":
    main()


