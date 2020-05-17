userwords = input("Введите свои слова: ")
words = []
words.append(userwords)
for ind, el in enumerate(userwords.split(" "), 1):
    print(ind, el)
