# https://www.nowcoder.com/ta/huawei
# HJ76

def cal(n):
    start = 0
    for i in range(1, n):
        start += i
    start = start * 2 + 1
    tar = n * n * n
    res = ''
    sum_v = 0
    while True:
        res += str(start)
        sum_v += start
        if sum_v == tar:
            print(res)
            return
        start += 2
        res += '+'


if __name__ == '__main__':
    s = input()
    cal(int(s))
