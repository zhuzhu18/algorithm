def merge(nums, tmp, l, r, rightEnd):       # 将两个已排序好的数组归并
    i, j = l, r
    k = l
    while i <= r - 1 and j <= rightEnd:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1
    while i < r:
        tmp[k] = nums[i]
        k += 1
        i += 1
    while j < rightEnd+1:
        tmp[k] = nums[j]
        k += 1
        j += 1
    for t in range(l, rightEnd+1):   # 将归并后的tmp倒回到nums的起始到终点位置
        nums[t] = tmp[t]

def divide(nums, tmp, l, rightEnd):
    if l < rightEnd:
        center = (l + rightEnd) // 2
        divide(nums, tmp, l, center)    # 递归的进行划分
        divide(nums, tmp, center+1, rightEnd)
        merge(nums, tmp, l, center+1, rightEnd)

def mergeSort(nums):
    tmp = [0 for _ in nums]
    divide(nums, tmp, 0, len(nums)-1)

a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
mergeSort(a)
print(a)
