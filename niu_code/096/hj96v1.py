# https://www.nowcoder.com/ta/huawei
# HJ96

n = input()
m = ''
x = False

for t in n:
    if t.isdigit():
        if x == False:
            m += '*'
        x = True
    else:
        if x:
            m += '*'
            x = False
    m += t
if x:
    m += '*'
print(m)