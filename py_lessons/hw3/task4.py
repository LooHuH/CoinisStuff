def count_repeated_pairs(string):
    count = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
    print("Amount of pairs: ", count)

result = count_repeated_pairs(input("Enter string >>> "))
