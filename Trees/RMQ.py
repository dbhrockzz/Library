import sys
#from collections import defaultdict
n,q = map(int,raw_input().strip().split())
A = [0]+map(int,raw_input().strip().split())
tree = {}

def build(node, start, end):
    if start==end:
        tree[node] = A[start]
    else:
        mid = (start+end)/2
        build(2*node, start, mid)
        build(2*node+1, mid+1, end)
        tree[node] = min(tree[2*node],tree[2*node+1])

def update(node, start, end, idx, val):
    if start==end:
        tree[node] = val
        A[idx] = val
    else:
        mid = (start+end)/2
        if idx>=start and idx<=mid:
            update(2*node, start, mid, idx, val)
        else:
            update(2*node+1, mid+1, end, idx, val)
        tree[node] = min(tree[2*node],tree[2*node+1])

def query(node, start, end, l, r):
    if r<start or end<l:
        return sys.maxint    
    elif l<=start and end<=r:
        return tree[node]
    mid = (start+end)/2
    p1 = query(2*node, start, mid, l, r)
    p2 = query(2*node+1, mid+1, end, l, r)
    return min(p1,p2)

build(1,1,n)
for i in range(q):
    s = raw_input().split()
    if s[0]=='q':
        print query(1,1,n,int(s[1]),int(s[2]))
    elif s[0]=='u':
        update(1,1,n,int(s[1]),int(s[2]))
