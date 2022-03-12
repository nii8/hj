# https://www.nowcoder.com/practice/9566499a2e1546c0a257e885dfdbf30d?tpId=37&tqId=21277&rp=1&ru=/ta/huawei&qru=/ta/huawei&difficulty=&judgeStatus=&tags=/question-ranking

from hj54v1 import get_c_list,cal_3_num

# v2版本是在v1版本上的改进
# 把c_list看成一个栈，如果遇到左括号标记一下索引，
# 遇到右括号再标记索引，把刚刚距离最近的左括号，到右括号之间的数字和操作符号，
# 传给一个函数去计算(里面肯定是没有括号的)，传出去的数字和操作符号，看成出栈。
# 把结果再进栈，还有后面的元素也全部进栈。然后循环这个操作得到最终结果。


# 这个列表的元素是数字和操作符号，没有括号，注意乘法优先级高
def cal_n_num(c_list):
    while True:
        if '*' not in c_list and '/' not in c_list:
            break
        for i, once in enumerate(c_list):
            if once == '*' or once == '/':
                x = c_list[i - 1]
                y = c_list[i + 1]
                num = cal_3_num(x, once, y)
                c_list[i - 1] = num
                del c_list[i]
                del c_list[i]
                break
    while True:
        if '+' not in c_list and '-' not in c_list:
            break
        for i, once in enumerate(c_list):
            if once == '+' or once == '-':
                x = c_list[i - 1]
                y = c_list[i + 1]
                num = cal_3_num(x, once, y)
                c_list[i - 1] = num
                del c_list[i]
                del c_list[i]
                break
    return c_list[0]

# 计算一次c_list中最内层括号中的表达式的值并替换
def cal_k(c_list):
    k_list = []
    l = None
    r = None
    k_done = False
    for i,once in enumerate(c_list):
        if k_done:
            k_list.append(once)
            continue
        if once == '(':
            l = i
        if l != None and once == ')':
            r = i
            ret = cal_n_num(c_list[l+1:r])
            k_list[l] = ret
            k_list = k_list[:l+1]
            k_done = True
            continue
        k_list.append(once)
    if '(' in k_list:
        return False, k_list
    else:
        return True, k_list

# 通过cal_k循环多次,消灭c_list中所有的括号
def cal_k_all(c_list):
    while True:
        ret,c_list = cal_k(c_list)
        if ret:
            break
    return c_list

def cal(s):
    c_list = get_c_list(s)
    c_list = cal_k_all(c_list)
    return cal_n_num(c_list)

if __name__ == '__main__':
    s = input()
    print(cal(s))