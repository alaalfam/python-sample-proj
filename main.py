import re


def element_is_not_float(param):
    try:
        res = float(param)
        return False
    except ValueError:
        return True


def remove_string_from_list(list):
    i = 0
    while i < len(list):
        if element_is_not_float(list[i]):
            list.pop(i)
            continue
        i += 1
    return list


if __name__ == '__main__':
    str = input()
    list = re.split(r'[,\s+\']', str)
    print(list)
    list = remove_string_from_list(list)
    result = sum(map(float, list))
    print(result)
