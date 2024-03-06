from random import randint as r

def generated_list_of_points():
    class Points:
        def __init__(self) -> None:
            self.math = r(0, 50)
            self.programming = r(0, 50)
            self.sum = self.math + self.programming
    people = []
    for _ in range(10):
        people.append(Points())
    return people

results = generated_list_of_points()

all_sums = [piece.sum for piece in results]
max_sum = max(all_sums)
if all_sums.count(max_sum) > 1:
    all_programming_points = [piece.programming for piece in results]
    max_programming_points = max(all_programming_points)
    winner_num = all_programming_points.index(max_programming_points) + 1
else:
    winner_num = all_sums.index(max_sum) + 1
    
print(f'Winner - #{winner_num}/#10 with {max_sum} sum points',
      f'Math points - {results[winner_num-1].math}',
      f'Programming points - {results[winner_num-1].programming}',
      sep='\n')
    

