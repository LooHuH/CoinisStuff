from askvar import askvar

objects = ['arrow', 'target']
all_cords = {}
for arg in objects:
    cords = {}
    for number in [1, 2]:
        xy_cords = {}
        for cord_name in ['x', 'y']:
            cord = askvar(f'coordinate {cord_name}{number} for {arg}')
            xy_cords[cord_name] = cord
        cords[number] = xy_cords
    all_cords[arg] = cords