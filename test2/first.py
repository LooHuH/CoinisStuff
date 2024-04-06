import csv


def read_nums(file_name, column_num):
    with open(file_name) as file:
        csv_reader = csv.reader(file)
        __nums = []
        __column_name = None
        for row in csv_reader:
            __row_len = len(row)
            __column = column_num - 1
            item = row[__column]
            try:
                item = float(item)
                __nums.append(item)
            except Exception:
                if not __column_name:
                    __column_name = item
        return __row_len, __column_name, __nums


row_len, column_name, nums = read_nums('data.csv', 2)
print(f'Min {column_name} - {min(nums)}',
      f'Max {column_name} - {max(nums)}',
      sep='\n')

for column in range(2, row_len):
    row_len, column_name, nums = read_nums('data.csv', column)
    if not nums:
        break
    average = sum(nums) / len(nums)
    print(f'Average of {column_name} - {round(average, 5)}')

for column in range(2, row_len):
    row_len, column_name, nums = read_nums('data.csv', column)
    if not nums:
        break
    average = sum(nums) / len(nums)
    percentage = average / max(nums)
    print(f'middle/average percentage - {round(100*(percentage), 2)}')
