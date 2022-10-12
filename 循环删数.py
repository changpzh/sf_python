"""
有一个数组 a[N] 顺序存放 0 ~ N-1 ，要求每隔两个数删掉一个数，到末尾时循环至开头继续进行，求最后一个被删掉的数的原始下标位置。
以 8 个数 (N=7) 为例 :｛ 0，1，2，3，4，5，6，7 ｝，0 -> 1 -> 2 (删除) -> 3 -> 4 -> 5 (删除) -> 6 -> 7 -> 0 (删除),
如此循环直到最后一个数被删除。

数据范围：

输入描述:
每组数据为一行一个整数n(小于等于1000)，为数组成员数

输出描述:
一行输出最后一个被删掉的数的原始下标位置。
输入例子1:
8

输出例子1:
6

输入例子2:
1

输出例子2:
0
"""

"""
循环删除的思路-先求出下次起始删除位置后，再进行本次删除
【本方法只针对间隔两位数有效，】
1. 根据输入数字，形成需要被删除的列表
2. 获得间隔多少个数interval进行删除，从而求出列表切片中的步长step = interval + 1
3. while len（list）> 1：
    3.1 如果剩余列表 长度大于1，且小于等于2时：
        删除起始位置为原位置对 间隔interval取余
    3.2 否则    
        3.2.1 先求下次删除的初始位置，根据结束位置可以知道下次初始位置
            idx = start
            while True:
                if s_list[idx] == s_list[-3]:
                    start = 0
                    break
                elif s_list[idx] == s_list[-2]:
                    start = 1
                    break
                elif s_list[idx] == s_list[-1]:
                    start = 2
                    break
                idx += step    

        3.2.2 执行删除 del s_list[del_start::step]
4. 最后列表只剩下最后一个数，即为列表的下标，打印list[0]
        

"""

while True:
    try:
        input_num = int(input())
        s_list = [i for i in range(input_num)]
        # s_list = [i for i in range(1)]
        interval = 2
        start = interval
        step = interval + 1
        while len(s_list) > 1:
            if 1 < len(s_list) <= interval:
                del_start = start % interval
                # TODO 需要添加interval是任意值的时候的start值变化。
            else:
                del_start = start
                idx = start
                outer_break = False
                while True:
                    for i in range(step):
                        if s_list[idx] == s_list[-(i + 1)]:
                            start = interval - i
                            outer_break = True
                            break
                    if outer_break:
                        break
                    idx += step

            del s_list[del_start::step]
        print(s_list[0])

    except:
        break
