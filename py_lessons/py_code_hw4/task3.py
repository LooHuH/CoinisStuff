students = [
    {'name': 'Ana', 'age': 22, 'average': 9.1},
    {'name': 'Ivan', 'age': 20, 'average': 8.5},
    {'name': 'Petra', 'age': 25, 'average': 9.8},
    {'name': 'Marko', 'age': 23, 'average': 8.9}
]

age_filter = lambda student: student['age'] >= 21
filtered_students = list(filter(age_filter, students))

average = lambda student: student['average']
sorted_filtered_students = sorted(filtered_students, key=average)
print(sorted_filtered_students)
