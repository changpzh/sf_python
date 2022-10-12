"""
描述
给定一个长度为n的数组nums，数组由一些非负整数组成，现需要将他们进行排列并拼接，每个数不可拆分，使得最后的结果最大，返回值需要是string类型，否则可能会溢出。

数据范围：1 \le n \le 1001≤n≤100，0 \le nums[i] \le 100000≤nums[i]≤10000
进阶：时间复杂度O(nlogn)O(nlogn) ，空间复杂度：O(n)O(n)

示例1
输入：
[30,1]
返回值：
"301"

示例2
输入：
[2,20,23,4,8]
返回值：
"8423220"

示例3
输入：
[2]
返回值：
"2"

示例4
输入：
[10]
返回值：
"10"

备注：
输出结果可能非常大，所以你需要返回一个字符串而不是整数。
"""


class Solution:
    def solve(self, nums):
        nums_len = len(nums)
        if not nums[0]: # 全是0则删除一个0
            return '0'
        # 先转换为string列表
        num_strings = [str(num) for num in nums]

        # 最大的数放到第一个位置， 冒泡排序
        for i in range(nums_len - 1):
            for j in range(i + 1, nums_len):
                if int(num_strings[i] + num_strings[j]) < int(num_strings[j] + num_strings[i]):
                    num_strings[i], num_strings[j] = num_strings[j], num_strings[i]
        result = ''.join(num_strings)
        return result
