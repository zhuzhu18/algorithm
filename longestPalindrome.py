def longestPalindrome(s: str):
    if len(s) == 0:
        return ""
    location = [0, 0]    # 保存起始位置
    for i in range(len(s)):       # 遍历s中的每个字符, 更新回文子串起点和终点的位置, 即location
        i = findLongest(s, i, location)        # 把回文看成中间的部分全是同一字符，左右部分相对称
                                               # 找到下一个与当前字符不同的字符
    return s[location[0]: location[1]+1]

def findLongest(s: str, low: int, location: [int]):
    # 查找中间部分
    high = low
    while high < len(s) - 1 and s[high+1] == s[low]:
        high += 1         # 定位中间部分的最后一个字符
    ans = high
    # 从中间向左右扩散
    while low >= 0 and high < len(s):
        if low == 0 or high == len(s) - 1 or s[low-1] != s[high+1]:
            break
        else:
            low -= 1
            high += 1
    # 记录最大长度
    if high - low >= location[1] - location[0]:
        location[0] = low
        location[1] = high
    return ans

print(longestPalindrome('abcbdefghjhgf'))
