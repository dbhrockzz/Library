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

arr = map(int,raw_input().strip().split())
n = len(arr)
st = stack()
st.push(0)
ans = arr[:]

for i in range(1,n):
    while (not st.isEmpty()) and arr[i] < arr[st.peek()]:
        temp = st.pop()
        temp2 = -1
        if not st.isEmpty():
            temp2 = st.peek()
        ans[temp] = (i-temp2-1)*arr[temp]
    st.push(i)
while not st.isEmpty():
    temp = st.pop()
    temp2 = -1
    if not st.isEmpty():
        temp2 = st.peek()
    ans[temp] = (n-temp2-1)*arr[temp]
print max(ans)