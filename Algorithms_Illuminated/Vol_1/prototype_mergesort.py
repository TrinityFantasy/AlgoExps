import time as t


def merge(nums, lo, mid, hi):
    lf = mid - lo + 1
    lb = hi - mid

    L = [0] * (lf)
    R = [0] * (lb)

    for i in range(0, lf):
        L[i] = nums[lo + i]

    for j in range(0, lb):
        R[j] = nums[mid + 1 + j]

    i = 0
    j = 0
    k = lo

    while i < lf and j < lb:
        if L[i] <= R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1

    while i < lf:
        nums[k] = L[i]
        i += 1
        k += 1
    while j < lb:
        nums[k] = R[j]
        j += 1
        k += 1


def mergeSort(nums, lo, hi):
    if lo < hi:
        mid = lo + (hi - lo) // 2

        mergeSort(nums, lo, mid)
        mergeSort(nums, mid + 1, hi)
        merge(nums, lo, mid, hi)


if __name__ == "__main__":
    nums = [5, 4, 1, 8, 7, 2, 6, 3]
    l = len(nums)

    s = t.time()
    mergeSort(nums, 0, l - 1)
    e = t.time()
    cost = e - s
    print(f"Result of mergeSort is: {nums}, time cost is {cost} Sec.\n")
