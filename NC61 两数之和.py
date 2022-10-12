'''
描述
给出一个整型数组 numbers 和一个目标值 target，请在数组中找出两个加起来等于目标值的数的下标，返回的下标按升序排列。
（注：返回的数组下标从1开始算起，保证target一定可以由数组里面2个数字相加得到）


要求：空间复杂度 O(n)O(n)，时间复杂度 O(nlogn)O(nlogn)
示例1
输入：
[3,2,4],6

返回值：
[2,3]

说明：
因为 2+4=6 ，而 2的下标为2 ， 4的下标为3 ，又因为 下标2 < 下标3 ，所以返回[2,3]            
示例2
输入：
[20,70,110,150],90

返回值：
[1,2]

说明：
20+70=90     
'''


def twoSum(numbers: list[int], target: int) -> list[int]:
    # write code here
    res = []
    tmp_dict = {}
    for idx, number in enumerate(numbers):
        find_num = target - number
        if number in tmp_dict:
            res.append(tmp_dict[number] + 1)
            res.append(idx + 1)
        else:
            tmp_dict[find_num] = idx
    return res


print(twoSum([3, 2, 4], 6))
