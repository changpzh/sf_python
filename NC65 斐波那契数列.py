'''
描述
大家都知道斐波那契数列，现在要求输入一个正整数 n ，请你输出斐波那契数列的第 n 项。
斐波那契数列是一个满足 fib(x)=\left\{ \begin{array}{rcl} 1 & {x=1,2}\\ fib(x-1)+fib(x-2) &{x>2}\\ \end{array} \right.fib(x)={
1
fib(x−1)+fib(x−2)

x=1,2
x>2
  的数列
数据范围：1\leq n\leq 401≤n≤40
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n) ，本题也有时间复杂度 O(logn)O(logn) 的解法

输入描述：
一个正整数n
返回值描述：
输出一个正整数。
示例1
输入：
4
复制
返回值：
3
复制
说明：
根据斐波那契数列的定义可知，fib(1)=1,fib(2)=1,fib(3)=fib(3-1)+fib(3-2)=2,fib(4)=fib(4-1)+fib(4-2)=3，所以答案为3。
示例2
输入：
1
复制
返回值：
1
复制
示例3
输入：
2
复制
返回值：
1

'''
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param n int整型 
# @return int整型
#
#
# class Solution:
#     def Fibonacci(self, n: int) -> int:
#         # write code here
#         def fib(n):
#             a = b = 1
#             i = 0
#             while i < n:
#                 yield a
#                 a, b = b, a + b
#                 i += 1
#         num_list = [num for num in fib(n)]
#         return num_list[n-1]

input_num = int(input('输入数目:'))


def fib_generator(n):
    a = b = 1
    i = 0
    while i < n:
        yield a
        a, b = b, a + b
        i += 1


num_list = list(fib_generator(input_num))
print(num_list)



def fib_last(number):
    '''
    # 解法2，只返回斐波那契数列最后一个数。
    :param number:
    :return:
    '''
    if number < 1:
        return 0

    a, b = 0, 1
    for _ in range(number):
        a, b = b, a + b
    return b
