def insertSort(nums):
    n = len(nums)
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] <= nums[j]:   # 如果第i个元素比前面第j个元素小，则将它移至第j个元素处，后面的元素依次向后移动一个位置
                temp = nums[i]
                for k in range(i, j, -1):
                    nums[k] = nums[k-1]   # 依次向后移动一个位置
                nums[j] = temp
    return nums

a = [125, 130, 132, 123, 127, 129, 117, 121, 126, 116, 120, 122]
print(insertSort(a))
