"""
链接：https://www.nowcoder.com/questionTerminal/5382ff24fbf34a858b15f93e2bd85307
来源：牛客网

给定两个字符串 s和 t ，判断 s是否为 t 的子序列。
你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度n ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：时间复杂度O(n)\O(n) ，空间复杂度O(n)\O(n)

输入描述:
共两行，第一行为字符串s,  第二行为字符串t


字符串t的长度 1<=n<=500000


字符串s的长度 1<=m<=100

输出描述:
输出true或者是false，true表示是s是t的子序列，false表示s不是t的子序列

示例1
输入
abc
ahbgdc
输出
true

示例2
输入
axc
ahbgdc
输出
false
"""

"""
思路：
1. 
"""

MIN_LEN = 1
S_MAX_LEN = 100
T_MAX_LEN = 500000


def s_is_t(s, t):
    s_len = len(s)
    t_len = len(t)
    if s_len > t_len:
        return 'false'

    p1 = p2 = 0
    matched_letter = ''
    while p1 < s_len and p2 < t_len:
        if s[p1] == t[p2]:
            matched_letter += s[p1]
            p1 += 1
            p2 += 1
        else:
            p2 += 1

    if matched_letter == s:
        return 'true'
    return 'false'


while True:
    try:
        s = input('请输入字符串s（长度【1，100】）:') or 'tctpkc'
        t = input('请输入字符串t（长度【1，50w】）:') or 'tvctnpqxkcrnuufuctx'
        if MIN_LEN <= len(s) <= S_MAX_LEN and MIN_LEN <= len(s) <= T_MAX_LEN:
            print(s_is_t(s, t))
        else:
            print('Warning: 不符合字符输入长度，请重新输入！')
    except:
        break
