from askvar import askvar
import re

password = askvar('password', raw=True)

password_is_strong = re.search('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,100}$', password)

if password_is_strong:
    print('Pass is strong')
else:
    print('Create another password')