def mergeSort(nums):
    n = len(nums)
    if n == 1:
        return nums
    else:
        mid = int((n - 1) / 2)
        s1 = mergeSort(nums[:mid+1])     # 排序切分后的两个子集s1和s2
        s2 = mergeSort(nums[mid+1:])

        i = 0
        j = 0
        k = 0
        while i <= mid and j <= (n-mid-2):
            if s1[i] <= s2[j]:
                nums[k] = s1[i]         # i 遍历子集s1
                i += 1
                k += 1
            else:
                nums[k] = s2[j]         # j 遍历子集s2
                j += 1
                k += 1
            if i <= mid:         # 若子集s1中还有元素剩余，则直接拷贝给排序后数组nums剩余部分
                nums[k:n] = s1[i:mid+1]
            else:
                nums[k:n] = s2[j:(n-mid-1)]         # 若子集s2中还有元素剩余，则直接拷贝给排序后数组nums剩余部分
    return nums


a = [24, 17, 40, 28, 13, 14, 22, 32, 40, 21, 48, 4, 47, 8, 37, 18]
print(mergeSort(a))
