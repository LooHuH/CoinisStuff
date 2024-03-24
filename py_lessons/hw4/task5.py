from functools import reduce

students = [
    ('Ana', 8.5, 'Matematika'),
    ('Ivan', 9.2, 'Matematika'),
    ('Petra', 7.8, 'Fizika'),
    ('Marko', 8.9, 'Fizika'),
    ('Petra', 9.5, 'Matematika'),
    ('Marko', 7.6, 'Matematika'),
    ('Ana', 8.3, 'Fizika'),
    ('Ivan', 8.8, 'Fizika')
]

math_filter = lambda student: student[2] == 'Matematika'
math_students = list(filter(math_filter, students))
phys_filter = lambda student: student[2] == 'Fizika'
phys_students = list(filter(phys_filter, students))

grade_map = lambda student: student[1]
math_grades = list(map(grade_map, math_students))
phys_grades = list(map(grade_map, phys_students))

sum_reduce = lambda a, b: a + b
math_average_grade = reduce(sum_reduce, math_grades) / len(math_grades)
phys_average_grade = reduce(sum_reduce, phys_grades) / len(phys_grades)

answer = [('Matematika', math_average_grade), ('Fizika', phys_average_grade)]
print(answer)