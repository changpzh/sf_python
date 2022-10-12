"""
公司用一个字符串来标识员工的出勤信息

  absent:    缺勤
  late:      迟到
  leaveearly:早退
  present:   正常上班

  现需根据员工出勤信息,判断本次是否能获得出勤奖,
  能获得出勤奖的条件如下：
      1.缺勤不超过1次
      2.没有连续的迟到/早退
      3.任意连续7次考勤 缺勤/迟到/早退 不超过3次

   输入描述：
    用户的考勤数据字符串记录条数  >=1
    输入字符串长度 <10000 ;
    不存在非法输入
    如：
     2
     present
     present absent present present leaveearly present absent

    输出描述：
    根据考勤数据字符串
    如果能得到考勤奖输出true否则输出false
    对于输出示例的结果应为
     true false

    示例一：
     输入：
      2
      present
      present present

     输出：
      true true

    示例二
     输入：
      2
      present
      present absent present present leaveearly present absent
     输出：
      true false
"""

"""
算法思路-考勤信息

1. 接受用户输入数据
2. 验证数据合法性
3. 如果不合法
    抛出不合法信息，让用户重新输入
4. 如果合法
    定义获奖列表
    4.1对输入的考勤信息按行拆分为行列表
    4.2对每行进行如下操作
        根据空格拆分为出勤list
       4.2.1if 缺勤次数大于1 or 连续迟到/早退次>0 or 任意连续七天的缺勤/迟到/早退次数 > 3：
            获奖列表append("false")
            continue
       4.2.2获奖列表append('true')
   4.3返回结果
       列表转字符，以空格连接
       return 结果


4.2.1 是否缺勤次数大于1
    return list.count("缺勤")

4.2.2是否连续的迟到/早退次数大于0
    for i in range(len(list)-1):
        if (list[i] in ['迟到','早退']) and (list[i+1] in ['迟到','早退']):
            return True
    else:
        return False

4.2.3是否任意连续七天的缺勤/迟到/早退次数大于3
    for i in range(len(list)):
        tmp_list = list[i:i+7]
        tmp_total =0
        for 出勤 in tmp_list：
            if 出勤 in ['缺勤', '迟到','早退']：
                tmp ++
                if tmp >3:
                    return True
                else什么都不做
            else什么都不做
     return False

"""


def is_valid(num, a_list):
    return num >= 1


def absent_times(attendance_list):
    return attendance_list.count('absent')


# 4.2.2是否连续的迟到/早退次数大于0
#     for i in len(list)-1:
#         if (list[i] or list[i+1]) in ['迟到','早退']:
#             return True
#     else:
#         return False
def is_continual_late_or_leaveearly(attendance_list):
    for i in range(len(attendance_list) - 1):
        if (attendance_list[i] in ['late', 'leaveearly']) and (attendance_list[i + 1] in ['late', 'leaveearly']):
            return True
    else:
        return False


# 4.2.3是否任意连续七天的缺勤/迟到/早退次数大于3
#     for i in len(list)-7:
#         tmps = deepcopy(list[i:i+7])
#         tmp_total =0
#         for 出勤 in tmps：
#             if 出勤 in ['缺勤', '迟到','早退']：
#                 tmp_total ++
#                 if tmp_total >3:
#                     return True
#                 else什么都不做
#             else什么都不做
#      return False


def is_late_or_leaveearly_or_absent_bigger_than_3_in_any_continuous_7_days(attendance_list):
    list_len = len(attendance_list)
    if list_len < 7:
        return False

    for i in range(len(attendance_list)):
        tmp_list = attendance_list[i:i + 7]
        tmp_total = 0
        for attendance in tmp_list:
            if attendance in ['absent', 'late', 'leaveearly']:
                tmp_total += 1
                if tmp_total > 3:
                    return True
    else:
        return False


while True:
    # 1. 接受用户输入数据
    input_list = ["present", "present late present leaveearly present late present absent"]
    record_num = 2
    # record_num = int(input('请输入考勤条数：').strip())
    # for idx in range(record_num):
    #     input_list.append(input('请输入第%s考勤信息：' % (idx+1)).strip())

    # 2. 验证数据合法性
    # 3. 如果不合法
    #     抛出不合法信息，让用户重新输入
    if not is_valid(record_num, input_list):
        print('提示：输入不符合条件限制')
        print('请重新输入')
        continue
    # 4.如果合法
    else:
        res_list = []
        # 4.1对输入的考勤信息按行拆分
        # 4.2对每行进行如下操作
        #    根据空格拆分为出勤list
        #    4.2.1if 是否缺勤次数大于1 and 是否连续迟到/早退次>0 and 是否任意连续七天的缺勤/迟到/早退次数 > 3：
        #         获奖列表append("false")
        #         continue
        #    4.2.2获奖列表append('true')
        for tmp_str in input_list:
            attendance_list = tmp_str.split()
            if absent_times(attendance_list) > 1 or \
                    is_continual_late_or_leaveearly(attendance_list) or \
                    is_late_or_leaveearly_or_absent_bigger_than_3_in_any_continuous_7_days(attendance_list):
                res_list.append('false')
            else:
                res_list.append('true')

        # 4.3返回结果
        #     列表转字符，以空格连接
        #     return 结果
        print(' '.join(res_list))
        break
