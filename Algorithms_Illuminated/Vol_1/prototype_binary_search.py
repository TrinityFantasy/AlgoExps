import numpy as np
import time as t

def __read(fname):
    data = np.loadtxt(fname)
    ldata = len(data)

    return data,ldata

def __binSearch(key,arr,larr):
    lo = 0
    hi = larr-1
    mid = (lo+hi)//2

    while lo<hi:
        if arr[mid]>key:
            hi=mid-1
            mid=(lo+hi)//2
        elif arr[mid]<key:
            lo=mid+1
            mid=(lo+hi)//2
        else:
            return mid
        
if __name__ == "__main__":
    fpath = "/file/path/"
    fname = "largeText.txt"
    finput = fpath+fname

    data,ldata = __read(fname)
    #data,ldata = __read(finput)

    data = np.sort(data,kind='mergesort')

    key = 1201
    s = t.time()
    res = __binSearch(key,data,ldata)
    e = t.time()
    cost = e - s
    print(f'The 1st index of {key} is: {res}. Time cost is: {cost} Sec.\n')
