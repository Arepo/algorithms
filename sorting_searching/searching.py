import pdb

def bsearch(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = low + (high - low) // 2
        pdb.set_trace()
        if a[mid] < x:
           low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            return mid
    raise Exception

print(bsearch([5,6,7], 7))
