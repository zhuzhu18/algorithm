X = ['A', 'B', 'E', 'C', 'A', 'E', 'A', 'B']
Y = ['B', 'E', 'D', 'C', 'A', 'E', 'A']

def comSeq(x, y):
    c = [[0 for i in range(len(y) + 1)] for j in range(len(x) + 1)]
    rec = [[0 for i in range(len(y))] for j in range(len(x))]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i-1] != y[j-1]:
                u = c[i-1][j]
                l = c[i][j-1]
                if u >= l:
                    c[i][j] = u
                    rec[i-1][j-1] = 'U'
                else:
                    c[i][j] = l
                    rec[i-1][j-1] = 'L'
            else:
                c[i][j] = c[i-1][j-1] + 1
                rec[i-1][j-1] = 'LU'
    m = len(x) - 1
    n = len(y) - 1
    result = []
    while m >= 0 and n >= 0:
        if rec[m][n] == 'L':
            n -= 1
        if rec[m][n] == 'U':
            m -= 1
        else:
            result.append(X[m])
            n -= 1
            m -= 1
    result.reverse()
    return c[len(x)][len(y)], result

nums, seq = comSeq(X, Y)
print('最长公共子序列的元素个数:', nums)
print('最长的公共子序列是:', seq)
