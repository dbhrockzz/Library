def build(node, start, end):
    if start==end:
        tree[node] = A[start]
    else:
        mid = (start+end)/2
        build(2*node, start, mid)
        build(2*node, mid+1, end)
    
        tree[node] = tree[2*node]+tree[2*node+1]

def update(node, start, end, idx, val):
    if start==end:
        tree[node] += val
        A[idx] += val
    else:
        mid = (start+end)/2
        if idx>=start and idx<=mid:
            update(2*node, start, mid, idx, val)
        else:
            update(2*node+1, mid+1, end, idx, val)
        tree[node] = tree[2*node]+tree[2*node+1]

def query(node, start, end, l, r):
    if r<start or end<l:
        return 0    
    elif l<=start and end<=r:
        return tree[node]
    mid = (start+end)/2
    p1 = query(2*node, start, mid, l, r)
    p2 = query(2*node+1, mid+1, end, l r)
    return p1+p2

