def kadalgo(arr):
    n = len(arr)
    max_so_far = 0
    max_ending = 0
    for i in range(n):
        max_ending += arr[i]
        if max_ending<0:
            max_ending=0
        if max_so_far<max_ending:
            max_so_far=max_ending
    return max_so_far
