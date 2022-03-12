# https://www.nowcoder.com/ta/huawei
# HJ14

count = int(input())
c_list = []

for tmp in range(count):
    s = input()
    c_list.append(s)
c_list.sort()
for x in c_list:
    print(x)
