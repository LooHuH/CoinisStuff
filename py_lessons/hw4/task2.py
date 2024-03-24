from functools import reduce

students = ['Ana', 'Ivan', 'Milos', 'Jovana']
grades = [10, 2, 8.6, 6.7]

result = []
students_zip = zip(students, grades)
for student, grade in students_zip:
    if grade > 8.5:
        result.append((student, grade))
print(result)