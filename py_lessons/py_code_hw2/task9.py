from askvar import askvar

objects = ['window', 'curtain']
all_cords = {}
for arg in objects:
    cords = {}
    for number in [1, 2]:
        xy_cords = {}
        for cord_name in ['x', 'y']:
            cord = askvar(f'{arg} coordinate {cord_name}{number}')
            xy_cords[cord_name] = cord
        cords[number] = xy_cords
    all_cords[arg] = cords
    
print(all_cords)
for object in objects:
    all_cords[object]['diameter'] = (abs(all_cords[object][1]['x']
                                         - all_cords[object][2]['x'])
                                     + abs(all_cords[object][1]['y']
                                         - all_cords[object][2]['y']))**0.5

if all_cords[objects[1]]['diameter'] >= all_cords[objects[0]]['diameter']:
    print('Curtain is good')
else:
    print('Curtain is smol')