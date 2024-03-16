def check(l: list, attribute: object):
    check_list = []
    for item in l:
        check_result = attribute(item)
        check_list.append(check_result)
    return check_list