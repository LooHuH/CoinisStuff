import defs as f

def task2(list_in):
    couples = []
    nums = str(list_in[0])
    start_index = 0
    end_index = 1
    while end_index <= len(list_in):
        if end_index == len(list_in):
            result = {
                'num': int(nums[0]),
                'len': len(nums)
            }
            couples.append(result)
            break
        
        num = list_in[end_index - 1]
        next_num = list_in[end_index]
        if next_num == num:
            nums += str(next_num)
            end_index += 1
        else:
            result = {
                'num': int(nums[0]),
                'len': len(nums)
            }
            couples.append(result)
            start_index = end_index
            end_index = start_index + 1
            nums = str(list_in[start_index])
    
    multiplies = [couple['num'] ** couple['len'] for couple in couples]
    max_multiply = f.find_num(max, multiplies)
    max_couple = couples[max_multiply.i]
    print(f"{[max_couple['num'] for _ in range(max_couple['len'])]}, {max_multiply.num}")


task2([1, 4, 2, 2, 2, 4, 4])