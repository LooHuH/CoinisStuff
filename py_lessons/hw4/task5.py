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
print(math_students)
print(phys_students)
