# https://www.nowcoder.com/practice/9566499a2e1546c0a257e885dfdbf30d?tpId=37&tqId=21277&rp=1&ru=/ta/huawei&qru=/ta/huawei&difficulty=&judgeStatus=&tags=/question-ranking

def is_num(s):
    if s in ['(',')','*','/','+','-']:
        return False
    else:
        return True

# 获取表达式列表，内部的元素为整数字符串，或者是字符'()-+*/'中一种，到后来元素也可以是int，float数字
def get_c_list(s):
    c_list = []
    num = ''
    for i,once in enumerate(s):
    	# -号出现在开头,那么就是负数
        if i == 0 and once == '-':
            num = '-'
            continue
        # -号出现在(之后,那么就是负数
        if once == '-' and s[i-1] == '(':
            num = '-'
        elif is_num(once):
            num += once
        else:
            if num != '':
                c_list.append(num)
            c_list.append(once)
            num = ''
    if num != '':
        c_list.append(num)
    return c_list

# 输入3个元素，x,y为数字，o为+-*/,输出计算结果。
def cal_3_num(x,o,y):
    if isinstance(x,str):
        x = int(x)
    if isinstance(y,str):
        y = int(y)
    if o == '*':
        return x*y
    elif o == '/':
        return x/y
    elif o == '-':
        return x-y
    elif o == '+':
        return x+y
    else:
        print('error:',x,y,o)


# 把表达式列表内部有【数字*/数字】的计算并替换
# 假如输入列表[3*(2*4+6)],那么输出[3*(8+6)]
# 因为两个数字之间有*/优先级最高计算
def cal_op1(c_list):
    for index,once in enumerate(c_list):
        if once == '*' or once == '/':
            c1 = c_list[index-1]
            c2 = c_list[index+1]
            if is_num(c1) and is_num(c2):
                ret = cal_3_num(c1,once,c2)
#                 print(c1, once, c2, '=', ret)
                c_list[index - 1] = ret
                c_list.pop(index)
                c_list.pop(index)
                return True,c_list
    return False, c_list

# 表达式两个数字之间有*/优先级最高计算，循环反复这个过程，直到表达式没有变化为止。
def cal_op1_all(c_list):
    while True:
        ret, c_list = cal_op1(c_list)
        if not ret:
            return c_list

# i代表左括号的索引，j代表右括号的索引，计算这一对括号中的表达式的值
# 这一对括号中的计算一定是+-法，因为*/在之前反复计算*/运算cal_op1后被消灭了。
# 表达式的计算可能会是(1+2+3)，所有内部也要有循环
def cal_n_num(c_list,i,j):
    for once in range(int((j-i-2)/2)):
        c1 = c_list[i + 1]
        op = c_list[i + 2]
        c2 = c_list[i + 3]
        sum = cal_3_num(c1, op, c2)
        c_list[i + 1] = sum
        del c_list[i + 2]
        del c_list[i + 2]
    del c_list[i + 2]
    del c_list[i]
    return c_list

# 计算表达式中有括号的部分，它的优先级第二高
# 执行一次后会消除一对括号
def cal_k(c_list):
    l = None #左括号索引位置
    r = None #右括号索引位置
    for i,once in enumerate(c_list):
        if once == '(':
            l = i
        if l != None and once == ')':
            r = i
            c_list = cal_n_num(c_list,l,r)
            return True,c_list
    return False, c_list

# 反复执行消灭括号的运算，直到没有括号
# 每消灭一对括号需要再执行一次第一优先级的循环消灭*/运算cal_op1_all
def cal_k_all(c_list):
    while True:
        ret, c_list = cal_k(c_list)
        c_list = cal_op1_all(c_list)
        if not ret:
            return c_list

# 这是执行的最后一步，就是计算没有括号，没有*/的运算
# 就是多个数字和加减号的运算 如1+2-3+5
def cal_end(c_list):
    for once in range(int((len(c_list)-1)/2)):
        c1 = c_list[0]
        op = c_list[1]
        c2 = c_list[2]
        sum = cal_3_num(c1, op, c2)
        c_list[0] = sum
        del c_list[1]
        del c_list[1]
    return c_list[0]

# 计算主函数
def cal_num(s):
    c_list = get_c_list(s)
    c_list = cal_op1_all(c_list) #计算乘法除法
    c_list = cal_k_all(c_list) #计算括号
    return cal_end(c_list)
    

if __name__ == '__main__':
    s = input()
    ret = cal_num(s)
    print(ret)