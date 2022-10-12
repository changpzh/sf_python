"""
给定一个非空字符串S，其被N个‘-’分隔成N+1的子串，给定正整数K，要求除第一个子串外，其余的子串每K个字符组成新的子串，并用‘-’分隔。对于新组成的每一个子串，如果它含有的小写字母比大写字母多，则将这个子串的所有大写字母转换为小写字母；反之，如果它含有的大写字母比小写字母多，则将这个子串的所有小写字母转换为大写字母；大小写字母的数量相等时，不做转换。
输入描述:
输入为两行，第一行为参数K，第二行为字符串S。
输出描述:
输出转换后的字符串。
示例1
输入
3
12abc-abCABc-4aB@
输出
12abc-abc-ABC-4aB-@
说明
子串为12abc、abCABc、4aB@，第一个子串保留，后面的子串每3个字符一组为abC、ABc、4aB、@，abC中小写字母较多，转换为abc，ABc中大写字母较多，转换为ABC，4aB中大小写字母都为1个，不做转换，@中没有字母，连起来即12abc-abc-ABC-4aB-@
示例2
输入
12
12abc-abCABc-4aB@
输出
12abc-abCABc4aB@
说明
子串为12abc、abCABc、4aB@，第一个子串保留，后面的子串每12个字符一组为abCABc4aB@，这个子串中大小写字母都为4个，不做转换，连起来即12abc-abCABc4aB@
"""


def get_split(source_string, delimiter='-'):
    tmp_list = source_string.split(delimiter)
    return tmp_list[0], tmp_list[1:]


def change_to_string(s_list):
    return ''.join(s_list)


def split_by(split_num, source_string):
    str_list = []
    max_len = len(source_string)
    start_idx = 0
    end_idx = start_idx + split_num
    while start_idx < max_len:
        str_list.append(''.join(source_string[start_idx: end_idx]))
        start_idx = end_idx
        end_idx = start_idx + split_num
        end_idx = end_idx if end_idx < max_len else max_len
    return str_list


def change_case_if_needed(source_string):
    uppercase_num = 0
    lowercase_num = 0
    for letter in source_string:
        if letter.islower():
            lowercase_num += 1
        elif letter.isupper():
            uppercase_num += 1
    if uppercase_num > lowercase_num:
        return source_string.upper()
    elif uppercase_num < lowercase_num:
        return source_string.lower()
    return source_string


if __name__ == '__main__':
    split_num = int(input('请输入参数K：').strip())
    source_str = input('请输入需要分割的字符串：').strip()

    first_str, need_to_handle_list = get_split(source_str)
    all_character_string = change_to_string(need_to_handle_list)
    str_list = split_by(split_num, all_character_string)

    result_list = [first_str]
    for word in str_list:
        result_list.append(change_case_if_needed(word))
    result_string = '-'.join(result_list)
    print(result_string)
