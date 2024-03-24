from functools import reduce

l = ["flower", "flow", "flight"]
attr = lambda a, b: a if len(a) >= len(b) else b
result = reduce(attr, l)

print(f'First longest string - {result}')