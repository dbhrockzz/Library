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

def calSpan(price):
    n = len(price)
    ans = [0]*(n)
    st = stack()

    ans[0]=1
    st.push(0)
    for i in range(1,n):
        while (not st.isEmpty()) and price[st.peek()]<=price[i]:
            temp = st.pop()
        if st.isEmpty():
            ans[i] = i+1
        else:
            ans[i] = i-st.peek()
        st.push(i)
    return ans

arr = map(int,raw_input().strip().split())
print calSpan(arr)
