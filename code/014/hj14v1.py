count = int(input())
c_list = []
max_len = 0

for tmp in range(count):
    s = input()
    if len(s) > max_len:
        max_len = len(s)
    c_list.append(s)

cc_list = []
for x in c_list:
    sum_num = 0
    for i, y in enumerate(x):
        t = 0
        if y.isupper():
            t = ord(y) - 64
        else:
            t = ord(y) - 96 + 26
        sum_num += (53 ** (max_len - i - 1) * t)
    cc_list.append([sum_num, x])
cc_list.sort(key=(lambda x: x[0]))
for once in cc_list:
    print(once[1])