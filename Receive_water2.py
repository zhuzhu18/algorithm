def trap(height):
    stack = []
    res = 0
    for i, h in enumerate(height):
        while len(stack) > 0 and h > height[stack[-1]]:    # while循环表示比当前柱子低的元素都要出栈, 以维持一个单调递减栈
            tmp = stack.pop()      # 低洼处的位置
            if stack:     # 如果栈为空, 说明低洼处左边没有柱子了, 无法积水
                width = i - stack[-1] - 1     # 积水的宽度
                bounded_height = min(height[stack[-1]], h) - height[tmp]     # 积水的高度
                res += width * bounded_height
        stack.append(i)
    return res

h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
a = trap(h)
print(a)
