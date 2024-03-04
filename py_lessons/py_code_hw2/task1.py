from random import randint as r

portal_opened = 'Portal is opened'
portal_closed = 'Portal is still closed'

num = r(0, 100)

if num % 2 == 0:
    print(portal_opened)
else:
    print(portal_closed)