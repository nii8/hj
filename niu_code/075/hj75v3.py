# https://www.nowcoder.com/ta/huawei
# HJ75
# 动态规划，画出二维数组，第一行列的格子填充a，b

def cal(a,b):
    m = len(a)
    n = len(b)
    dp = []
    max_len = 0
    for i in range(m+1):
        dp.append([])
        for j in range(n+1):
            dp[i].append(0)
    for i in range(1,m+1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
            if dp[i][j]> max_len:
                max_len = dp[i][j]
    print(max_len)
    return max_len

if __name__ == '__main__':
    a = input()
    b = input()
    cal(a, b)