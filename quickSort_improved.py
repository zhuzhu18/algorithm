def median(nums, start, end):
    mid = (start + end) // 2
    if nums[start] > nums[end]:
        nums[start], nums[end] = nums[end], nums[start]
    if nums[mid] > nums[end]:
        nums[mid], nums[end] = nums[end], nums[mid]
    if nums[mid] < nums[start]:
        nums[mid], nums[start] = nums[start], nums[mid]
    return mid

def quickSort(nums, start, end):
    if start >= end:
        return
    mid = median(nums, start, end)
    pivot = nums[mid]
    nums[end], nums[mid] = nums[mid], nums[end]
    low = start
    high = end-1
    while True:
        while nums[low] <= pivot and low < high:
            low += 1
        while nums[high] >= pivot and low < high:
            high -= 1
        if low < high:
            nums[low], nums[high] = nums[high], nums[low]
        else:
            break
    nums[low], nums[end] = nums[end], nums[low]
    quickSort(nums, start, low-1)
    quickSort(nums, low+1, end)

nums = [5, 4, 3, 2, 1]
quickSort(nums, 0, len(nums)-1)
print(nums)
