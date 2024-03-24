from askvar import askvar

objects = ['table', 'ant']
all_cords = {}
for arg in objects:
    cords = {}
    for number in [1, 2]:
        if arg == 'ant' and number == 2:
            pass
        else:
            xy_cords = {}
            for cord_name in ['x', 'y']:
                cord = askvar(f'{arg} coordinate {cord_name}{number}')
                xy_cords[cord_name] = cord
            cords[number] = xy_cords
    all_cords[arg] = cords

tb_x_1 = all_cords['table'][1]['x']
tb_y_1 = all_cords['table'][1]['y']
tb_x_2 = all_cords['table'][2]['x']
tb_y_2 = all_cords['table'][2]['y']

ant_x = all_cords['ant'][1]['x']
ant_y = all_cords['ant'][1]['y']

if ((tb_x_2 >= ant_x >= tb_x_1 and ant_y == tb_y_1 or ant_y == tb_y_2)
        or (tb_y_2 >= ant_y >= tb_y_1 and ant_x == tb_x_1 or ant_x == tb_x_2)):
    print('ant is on the edge of the table')
else:
    print('ant is not on the edge of the table')
