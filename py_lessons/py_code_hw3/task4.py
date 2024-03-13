def count_repeated_pairs(string):
    count = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
    return count

input_string = input("Введите строку: ")
result = count_repeated_pairs(input_string)
print("Количество повторяющихся пар: ", result)
