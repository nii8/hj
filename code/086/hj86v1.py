# https://www.nowcoder.com/ta/huawei
# HJ86

def cal(n):
    m = ''
    while True:
        x = n % 2
        m += str(x)
        n = int(n / 2)
        if n == 0:
            break
    m_list = m.split('0')
    max_len = 0
    for x in m_list:
        if len(x) > max_len:
            max_len = len(x)
    print(max_len)


if __name__ == '__main__':
    while True:
        try:
            n = input()
            cal(int(n))
        except:
            break