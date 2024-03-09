from askvar import askvar

while True:
    nums = askvar('nums', raw=True).split()
    try:
        nums = [int(x) for x in nums]
        nums_new = []
        for x in nums:
            if x >= 0:
                nums_new.append(x)
        break
    except:
        print('err')

summ = sum(x for x in nums_new[::2])

print(f'Sum = {summ}') 