#include <bits/stdc++.h>
#define MAX 200000
#define MOD 1000000007
#define printn(arr,n) for(int i=0;i<n;i++){ cout << arr[i] << ' ';} cout<<endl;
#define print(arr,x,y) for(int i=x;i<=y;i++) { cout << arr[i] << ' ';} cout<<endl
using namespace std;
int tree[MAX];
int A[MAX];

void build(int node, int start, int end){
    //cout<<node<<start<<end<<endl;
    if(start==end){
        tree[node] = A[start];
    }
    else{
        int mid = (start+end)/2;
        build(2*node, start, mid);
        build(2*node+1, mid+1, end);
        tree[node] = tree[2*node]<tree[2*node+1]?tree[2*node]:tree[2*node+1];
    }
}

void update(int node, int start, int end, int idx, int val){
    if(start==end){
        A[idx] = val;
        tree[node] = val;
    }
    else{
        int mid = (start+end)/2;
        if(start<=idx && idx<=mid){
            update(2*node, start, mid, idx, val);
        }
        else{
            update(2*node+1, mid+1, end, idx, val);
        }
        tree[node] = tree[2*node]<tree[2*node+1]?tree[2*node]:tree[2*node+1];
    }
}

int query(int node, int start, int end, int l, int r){
    if(r < start || end < l){
        return MOD;
    }
    if(l<=start && end<=r){
        return tree[node];
    }
    int mid = (start+end)/2;
    int p1 = query(2*node, start, mid, l, r);
    int p2 = query(2*node+1, mid+1, end, l, r);
    int ans = p1<p2?p1:p2;
    return ans;
}

int main(){

    int n,q;
    cin>>n>>q;
    A[0] = 0;
    for(int i=0;i<n;i++) cin>>A[i+1];
    build(1,1,n);
    //print(tree,1,2*n-1);
    //print(A,1,n);
    for(int i=0;i<q;i++){
        char a;
        int b,c;
        cin >> a >> b >> c;
        if(a=='q'){
            cout << query(1,1,n,b,c) << endl;
        }
        else if(a=='u'){
            update(1,1,n,b,c);
        }
        //print(tree,1,2*n-1);
        //print(A,1,n);
    }
    return 0;
}