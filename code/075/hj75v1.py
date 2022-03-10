# https://www.nowcoder.com/ta/huawei
# HJ75

# 先找到短的字符串，暴力找出它所有子串，判断是不是b的子串
# 再找出最大长度
def cal(a,b):
    if len(a) > len(b):
        a,b = b,a
    len_a = len(a)
    max_len = 0
    for i in range(len_a):
        for j in range(len_a-i):
            zi_str = a[i:j+1+i]
            if zi_str in b and len(zi_str)>max_len:
                max_len = len(zi_str)
    print(max_len)
    return

if __name__ == '__main__':
    a = input()
    b = input()
    cal(a,b)