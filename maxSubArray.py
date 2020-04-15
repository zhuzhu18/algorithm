def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]
    else:
        mid = int(len(nums)/2 + 0.5)
        s1 = maxSubArray(nums[:mid])
        s2 = maxSubArray(nums[mid:])

        temp1 = []
        for i in range(mid-1, -1, -1):
            temp1.append(sum(nums[i:mid]))

        temp2 = []
        if mid < len(nums)-1:
            for j in range(mid + 1, len(nums), 1):
                temp2.append(sum(nums[mid:j]))
        else:
            temp2.append(nums[mid])
        s3 = max(temp1) + max(temp2)

        return max(s1, s2, s3)

nums = [1, -2, 4, 5, -2, 8, 3, -2, 6, 3, 7, -1]
print(maxSubArray(nums))
