def lengthOfLongestSubstring(s: str) -> int:
    ans = 0
    n = len(s)
    if n < 2:
        return n
    left = 0
    right = 0
    used = {i: False for i in s}
    while right < n:
        if used[s[right]] == False:
            used[s[right]] = True
            right += 1
        else:
            ans = max(ans, right - left)
            while left < right and s[left] != s[right]:
                used[s[left]] = False
                left += 1
            left += 1
            right += 1

    ans = max(ans, right - left)
    return ans
a = "abcbcbd"
print(lengthOfLongestSubstring(a))
