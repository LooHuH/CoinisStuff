from askvar import askvar

percentage = askvar('percentage of attendance', num_barrier=[0, 100])
works_completed = askvar('does all seminar projects done? (0 - no / 1 - yes)', num_barrier=[0, 1])

if percentage >= 75 and works_completed:
    print('You can go on exams')
else:
    print("You can't go on exams")