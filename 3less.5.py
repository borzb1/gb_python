def my_sum():
    sum_res = 0
    ex = True
    while ex == True:
        number = input('Вводите числа через пробел или Q, чтобы выйти - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'Q' or number[el] == 'q':
                ex = False
                break
            else:
                res += int(number[el])
        sum_res += res
        print(f'Сумма: {sum_res}')
    print(f'Вся сумма: {sum_res}')

my_sum()