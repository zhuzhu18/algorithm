def flat_array(nums):
    res = []
    helper(nums, res)
    return res

def helper(nums, res):
    if isinstance(nums, list):
        for item in nums:
            temp = []
            helper(item, temp)
            res.extend(temp)
    else:
        res.append(nums)
    return res

a = [1, 2, 3, [4, 5, [5, 6], 7, 8], 9, [10, 11, [12]]]
b = flat_array(a)
print(b)
