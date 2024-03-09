from askvar import askvar

study_price = askvar('study price')
student_average_points = askvar('average points', num_barrier=[2, 5])
student_has_prize = askvar('student won a prize', num_barrier=[0, 1])

point_5_k = 0.6
point_4_k = 0.8
point_3_k = 0.9
prize_k = 0.7

student_k = []

if student_average_points == 5:
    student_k.append(point_5_k)
elif student_average_points >= 4:
    student_k.append(point_4_k)
elif student_average_points >= 3:
    student_k.append(point_3_k)

if student_has_prize:
    student_k.append(prize_k)
    
best_k = min(student_k)

new_price = round(study_price * best_k)

print(f'Study price - {new_price}')