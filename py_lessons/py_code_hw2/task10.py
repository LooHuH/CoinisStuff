from askvar import askvar

objects = ['target', 'arrow']
all_cords = {}
for object_index in range(len(objects)):
    info = {}
    for cord_name in ['x', 'y']:
        cord = askvar(f'coordinate {cord_name} for {objects[object_index]}')
        info[cord_name] = cord
    if object_index == 0:
        r = askvar('target radius')
        info['radius'] = r
    all_cords[objects[object_index]] = info
    
print(all_cords)

tgt_x = all_cords['target']['x']
tgt_y = all_cords['target']['y']
tgt_r = all_cords['target']['radius']

arrow_x = all_cords['arrow']['x']
arrow_y = all_cords['arrow']['y']

# check if arrow in target range
if ((tgt_x - tgt_r <= arrow_x <= tgt_x + tgt_r)
        and (tgt_y - tgt_r <= arrow_y <= tgt_y + tgt_r)):
    a = abs(arrow_x - tgt_x)
    b = abs(arrow_y - tgt_y)
    d = (a**2 + b**2)**0.5
    
    # check if arrow hits
    if d <= tgt_r:
        print('arrow hit')
    else:
        print('arrow miss')

else:
    print('arrow not in target range')
