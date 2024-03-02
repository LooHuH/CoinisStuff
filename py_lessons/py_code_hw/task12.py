from askvar import askvar
from datetime import datetime

years = askvar('years')
now = datetime.now().year

birth_year = now - years

print(f"Milos's birth year - {birth_year}")

