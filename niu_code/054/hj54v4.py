# https://www.nowcoder.com/practice/9566499a2e1546c0a257e885dfdbf30d?tpId=37&tqId=21277&rp=1&ru=/ta/huawei&qru=/ta/huawei&difficulty=&judgeStatus=&tags=/question-ranking

# 使用双栈的方法
# st1记录运算数字,st2记录运算符

# s = 1+2*3 st1 = [1,2,3]  st2 = [+,*]
def cal_num(st1, st2):
    b = st1[-1]
    del st1[-1]
    a = st1[-1]
    del st1[-1]
    op = st2[-1]
    del st2[-1]
    if op == '+':
        a = a + b
    elif op == '-':
        a = a - b
    elif op == '*':
        a = a * b
    elif op == '/':
        a = a / b
    st1.append(a)
    return st1, st2

# 比较运算符
def compare_op(m, n):
    if m == '(':        # 括号优先级最高
        return False
    elif m in ['+','-'] and n in ['*','/']:     # 乘除法比加减法优先级高  下面就不会1+2,因为s[i] = *
        return False                            # st1 = [1,2]  m = st2 = [+]  n = s[i] = *
    else:
        return True

def cal(s):
    st1, st2 = [], ['(']
    s += ')'
    flag = False    # 在数字进入st1后,flag置True,遇到+-*/后,通过compare_op判断执行顺序
    i = 0
    while i < len(s):
        if s[i] == '(':
            st2.append('(')
        elif s[i] == ')':
            while st2[-1] != '(':
                st1, st2 = cal_num(st1, st2)
            del st2[-1]
        elif flag:
            while compare_op(st2[-1], s[i]):
                st1, st2 = cal_num(st1, st2)
            st2.append(s[i])
            flag = False
        else:
            num = ''
            if s[i] == '-':
                num = '-'
                i += 1
            while s[i].isdigit():
                num += s[i]
                i += 1
            i -= 1
            st1.append(int(num))
            flag = True
        i += 1
    return st1[0]

if __name__ == '__main__':
    s = input()
    print(cal(s))