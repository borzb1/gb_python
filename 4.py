userwords = input("Введите свои слова через пробел: ")
words = []
words.append(userwords)
for ind, el in enumerate(userwords.split(" "), 1):
    print(ind, el[:10])

