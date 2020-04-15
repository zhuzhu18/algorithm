def selectSort(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[j] < nums[i]:      # 将当前元素与它之后的每一个元素作比较，找出最小的元素放在当前位置上
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
    return nums

a = [125, 130, 132, 123, 127, 129, 117, 121, 126, 116, 120, 122]
print(selectSort(a))
