"""
字符串回文指该字符串正序与其逆序逐字符一致。

数据范围：0 < n \le 10000000<n≤1000000
要求：空间复杂度 O(1)O(1)，时间复杂度 O(n)O(n)
示例1
输入：
"absba"

返回值：
true

示例2
输入：
"ranko"

返回值：
false

示例3
输入：
"yamatomaya"

返回值：
false

示例4
输入：
"a"

返回值：
true

备注：
字符串长度不大于1000000，且仅由小写字母组成
"""


class Solution:
    def judge(self, str: str) -> bool:
        # write code here
        return str[::-1] == str
