# https://www.nowcoder.com/ta/huawei
# HJ75

def cal(a,b):
    try:
        if len(a) > len(b):
            a,b = b,a
        max_length = 0
        i = 0
        while i + max_length < len(a):
            while i + max_length < len(a) and a[i:i + max_length + 1] in b:
                max_length += 1
            i += 1
        print(max_length)
        return max_length
    except:
        return 0


if __name__ == '__main__':
    a = input()
    b = input()
    cal(a, b)