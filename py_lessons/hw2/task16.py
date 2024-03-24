from askvar import askvar

objects = ['rectange', 'point']
all_cords = {}
for arg in objects:
    cords = {}
    for number in [1, 2]:
        if arg == objects[1] and number == 2:
            pass
        else:
            xy_cords = {}
            for cord_name in ['x', 'y']:
                cord = askvar(f'{arg} coordinate {cord_name}{number}')
                xy_cords[cord_name] = cord
            cords[number] = xy_cords
    all_cords[arg] = cords

rc_x_1 = all_cords['rectange'][1]['x']
rc_y_1 = all_cords['rectange'][1]['y']
rc_x_2 = all_cords['rectange'][2]['x']
rc_y_2 = all_cords['rectange'][2]['y']

point_x = all_cords['point'][1]['x']
point_y = all_cords['point'][1]['y']

if (rc_x_1 <= point_x <= rc_x_2) and (rc_y_2 <= point_y <= rc_y_1):
    print('point is in rectange')
else:
    print('point is not in rectange')