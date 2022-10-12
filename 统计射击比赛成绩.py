"""
给定一个射击比赛成绩单
  包含多个选手若干次射击的成绩分数
  请对每个选手按其最高三个分数之和进行降序排名
  输出降序排名后的选手id序列
  条件如下
    1. 一个选手可以有多个射击成绩的分数，且次序不固定
    2. 如果一个选手成绩少于3个，则认为选手的所有成绩无效，排名忽略该选手
    3. 如果选手的成绩之和相等，则相等的选手按照其id降序排列

   输入描述:
     输入第一行
         一个整数N
         表示该场比赛总共进行了N次射击
         产生N个成绩分数
         2<=N<=100

     输入第二行
       一个长度为N整数序列
       表示参与每次射击的选手id
       0<=id<=99

     输入第三行
        一个长度为N整数序列
        表示参与每次射击选手对应的成绩
        0<=成绩<=100

   输出描述:
      符合题设条件的降序排名后的选手ID序列

   示例一
      输入:
        13
        3,3,7,4,4,4,4,7,7,3,5,5,5
        53,80,68,24,39,76,66,16,100,55,53,80,55
      输出:
        5,3,7,4
      说明:
        该场射击比赛进行了13次
        参赛的选手为{3,4,5,7}
        3号选手成绩53,80,55 最高三个成绩的和为188
        4号选手成绩24,39,76,66  最高三个成绩的和为181
        5号选手成绩53,80,55  最高三个成绩的和为188
        7号选手成绩68,16,100  最高三个成绩的和为184
        比较各个选手最高3个成绩的和
        有3号=5号>7号>4号
        由于3号和5号成绩相等  且id 5>3
        所以输出5,3,7,4
"""

"""
算法思路分析：
算法-射击分数统计

接受输入
验证输入信息合法性
如果不合法
    抛出异常信息，让重新输入
否则合法
    4.1 将选手id和自己每次成绩关联，方法zip
    4.2 迭代4.1数据，将每名运动员比赛信息归档，使用dict，dict格式采用｛id:｛scores:[],id:id, total_valid_score:0｝，…｝
    4.3 删除成绩少于3个的运动员 
    4.4 计算运动员的前三高成绩的总成绩，存储到总分total_valid_score。
    4.5排序，将dict的values存入列表中排序，按照总分第一排序，第二排序为id，逆序
    4.6 根据排序列表找到运动员的排序id
    4.7 返回排好序的id字符串，空格隔离

备注：4.3和4.4可以合并在一次遍历里面进行，减少一次遍历
"""


from copy import deepcopy

VALID_LEN = 3


def build_dict(ids, scores):
    player_dict = {}
    id_score_pairs = zip(ids, scores)
    for p_id, score in id_score_pairs:
        if p_id in player_dict.keys():
            player_dict[p_id]['scores'].append(score)
        else:
            player_dict[p_id] = {'scores': [score], 'id': p_id}
    return player_dict


def remove_invalid_player_and_add_total_score(source_dict):
    def calculate_total_score(scores):
        total_score = 0
        for idx in range(VALID_LEN):
            total_score += scores[idx]
        return total_score

    tmp_dict = deepcopy(source_dict)
    for key, value in tmp_dict.items():
        scores_len = len(value['scores'])
        if scores_len < VALID_LEN:
            source_dict.pop(key)
            continue
        value['scores'].sort(reverse=True)
        source_dict[key]['total_score'] = calculate_total_score(value['scores'])


def get_ranked_ids(sorted_list):
    result_ranks = []
    for item in sorted_list:
        result_ranks.append(str(item['id']))
    return result_ranks


def solve(ids, scores):
    player_dict = build_dict(ids, scores)
    remove_invalid_player_and_add_total_score(player_dict)
    players = list(player_dict.values())
    print(players)
    sorted_players = sorted(players, key=lambda item: (item['total_score'], item['id']), reverse=True)
    ranked_id_list = get_ranked_ids(sorted_players)
    return ','.join(ranked_id_list)
    # print(','.join(ranked_id_list))


def is_input_valid(num, ids, scores):
    return True


# num = 13
# ids = [3, 3, 7, 4, 4, 4, 7, 7, 5, 3, 5, 5, 5]
# scores = [53, 80, 68, 24, 39, 76, 66, 16, 100, 55, 53, 80, 55]

while True:
    try:
        num = int(input().strip())
        ids = [int(p_id) for p_id in input().split(',')]
        scores = [int(score) for score in input().split(',')]
        print(ids)

        if is_input_valid(num, ids, scores):
            solve(ids, scores)
    except:
        break


