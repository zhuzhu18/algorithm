def quickSort(nums, start, end):
    if start >= end:
        return
    pivot = nums[start]
    low, high = start, end
    while low < high:
        while nums[high] >= pivot and low < high:
            high -= 1
        if low < high:
            nums[start] = nums[high]
        while nums[low] <= pivot and low < high:
            low += 1
        if low < high:
            nums[start] = nums[low]
    nums[low] = pivot
    quickSort(nums, start, low-1)
    quickSort(nums, low+1, end)
nums = [5, 4, 3, 2, 1]
quickSort(nums, 0, len(nums)-1)
print(nums)
