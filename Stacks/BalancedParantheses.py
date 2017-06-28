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
    s = raw_input("Enter the expression: ")
    st = stack()
    open_brackets = ['(','[','{']
    close_brackets = [')',']','}']
    d = {')':'(',']':'[','}':'{'}
    for char in s:
        if char in open_brackets:
            st.push(char)
        elif char in close_brackets:
            if st.isEmpty() or st.pop()!=d[char]:
                print "Invalid Expression"
                return
    if st.isEmpty():
        print "Valid Expression"
    else:
        print "Invalid Expression"

if __name__=="__main__":
    main()            
