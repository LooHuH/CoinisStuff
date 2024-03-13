def task2(list_in):
    different_nums = list(set(list_in))
    couples = []
    nums = list_in[0]
    start_index = 0
    end_index = 1
    while start_index < len(list_in) - 1:
        num = int(list_in[end_index - 1])
        next_num = int(list_in[end_index])
        if next_num == num:
            nums += str(next_num)
            end_index += 1
        else:
            result = {
                'nums': nums,
                'len': len(nums)
            }
            couples.append(result)
            start_index = end_index
            end_index = start_index + 1
            nums = list_in[start_index]
    all_lens = [couple['len'] for couple in couples]
    max_len = max(all_lens)
    max_len_couple_index = all_lens.index(max_len)
    
    multiplies = [num ** (list_in.count(num)) for num in different_nums]
    max_multi = max(multiplies)
    max_multi_num = different_nums[multiplies.index(max_multi)]
    print(f'{[max_multi_num for _ in range(list_in.count(max_multi_num))]}, {max_multi}')


task2([1, 4, 2, 2, 2, 4, 4])