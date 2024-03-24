from askvar import askvar

while True:
    current_hour = askvar('current hour', num_barrier=[0, 23])

    if ((current_hour >= 6
         and current_hour < 13)
        or (current_hour >= 17
            and current_hour < 22)):
        print("You can build stuff")
    else:
        print("You can't build stuff")
    