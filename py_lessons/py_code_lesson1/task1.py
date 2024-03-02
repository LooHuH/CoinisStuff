from cv2 import multiply
from askvar import askvar

code = askvar(varname='code', len_barrier=[3, 3], raw=True)

a = int(code[0])
b = int(code[1])
c = int(code[2])

ans = (a * b * c) - (a + b + c)

print(f'Answer - {ans}')
