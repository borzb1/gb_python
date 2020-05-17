my_list = []
n = int(input("Введите количество элементов : "))

for i in range(0, n):
    element_add = (input())

    my_list.append(element_add)

j = 0
for i in range(int(len(my_list) / 2)):
    my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    j += 2

print(my_list)