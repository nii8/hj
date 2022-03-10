# https://www.nowcoder.com/ta/huawei
# HJ85

def is_hui(s):
    src_len = len(s)
    if len(s) % 2 == 0:
        s_len = int(len(s)/2)
        s = s[:s_len] + 'a' + s[s_len:]
    s_len = int((len(s)-1) / 2)
    if s[:s_len] == s[s_len+1:][::-1]:
        return src_len
    else:
        return 0

def cal(s):
    s_len = len(s)
    max_len = 0
    for i in range(s_len-1):
        num = int((s_len - i)/2)
        for j in range(s_len-i):
            tmp = s[i:i+j+1]
            t_len = is_hui(tmp)
            if t_len > max_len:
                max_len = t_len
    print(max_len)
    return max_len


if __name__ == '__main__':
    s = input()
    cal(s)