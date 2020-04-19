x = [1, 3, 7, 10, 12, 17, 23, 26, 28, 29, 32]
target = 30

def binary_search(x, target):
    left = 0
    right = len(x) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if x[mid] > target:
            right = mid - 1
        elif x[mid] < target:
            left = mid + 1
        else:
            return mid
    return 'null'

index = binary_search(x, target)
print('查找到的该元素索引为:', index)
