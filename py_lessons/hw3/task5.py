import defs as f

movies = [{'naziv': 'Español para principiantes', 'br_pozitivni': 1000, 'br_negativni': 10},
          {'naziv': 'Philophize This!', 'br_pozitivni': 500, 'br_negativni': 30}, 
          {'naziv': 'Science VS.', 'br_pozitivni': 600, 'br_negativni': 45}]

def bad_percent(good_num, bad_num):
    return bad_num / (good_num + bad_num)

bad_k = []
for movie in movies:
    good_num = movie['br_pozitivni']
    bad_num = movie['br_negativni']
    bad_k.append(bad_percent(good_num, bad_num))
lowest_score = f.find_num(max, bad_k)
print(movies[lowest_score.i]['naziv'])
