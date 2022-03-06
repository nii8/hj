# https://www.nowcoder.com/practice/9566499a2e1546c0a257e885dfdbf30d?tpId=37&tqId=21277&rp=1&ru=/ta/huawei&qru=/ta/huawei&difficulty=&judgeStatus=&tags=/question-ranking

# 使用递归来计算，一气呵成。
# s是输入的字符串，始终不变,l和r代表的左右索引范围。
def cal(s,l,r):
    op = '+'    # 操作符初始为+
    num = 0
    st = []     # 代表stack，存储一个个数字，最后求和就是结果
                # 比如'1+2*2-3' ==> st = [1,4,-3]
    i = l       # 下面的循环代表从s的l遍历到r
    while i <= r:
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        if s[i] == '(':
            layer = 0
            j = i
            # 下面的循环就是要求出j的值
            # j代表是相对于i的这个左括号匹配的右括号的索引
            while j <= r:
                if s[j] == '(':
                    layer += 1
                elif s[j] == ')':
                    layer -= 1
                    if layer == 0:
                        break
                j += 1
            num = cal(s,i + 1, j - 1)   # 递归计算得到括号内部的值
            i = j # 这里括号内的值得到了，所以循环变量i应该跳跃到j，就是和i匹配的右括号的位置。
        if not s[i].isdigit() or i == r:
            if op == '+':
                st.append(num)
            elif op == '-':
                st.append(-num)
            elif op == '*':
                st[-1] *= num
            elif op == '/':
                st[-1] /= num
            op = s[i]
            num = 0
        i += 1
    res = 0
    for x in st:
        res += x
    return res

if __name__ == '__main__':
    s = input()
    print(cal(s,0,len(s)-1))