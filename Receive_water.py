def trap(height):
    res = 0
    for i in range(1, len(height)):
        left, right = i, i
        h1, h2 = height[i], height[i]
        while left >= 0:
            h1 = max(h1, height[left])
            left -= 1
        while right < len(height):
            h2 = max(h2, height[right])
            right += 1
        res += min(h1, h2) - height[i]
    return res

h = [0,1,0,2,1,0,1,3,2,1,2,1]
c = trap(h)
print(c)
