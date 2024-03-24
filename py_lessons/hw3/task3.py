def task3(nums_str):
    couples = []
    nums = all_nums[0]
    start_index = 0
    end_index = 1
    while end_index <= len(all_nums):
        if end_index == len(all_nums):
            result = {
                'nums': nums,
                'len': len(nums)
            }
            couples.append(result)
            break
        
        num = int(all_nums[end_index - 1])
        next_num = int(all_nums[end_index])
        if next_num == num - 1:
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
            nums = all_nums[start_index]
    all_lens = [couple['len'] for couple in couples]
    max_len = max(all_lens)
    max_len_couple_index = all_lens.index(max_len)
    print(f"Longest sawtooth - {couples[max_len_couple_index]['nums']}")


while True:
    all_nums = input('Enter integer string >>> ')
    if all_nums.isdigit():
        task3(all_nums)
        break