from askvar import askvar

num = askvar('num', needed_len=4, raw=True)
entry_num = int((int(num[1]) * int(num[3])) ** 0.5)

print(f'Entry number = {entry_num}')
