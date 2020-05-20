def user(name,surname, date, city, email, phone):
    print(f"{name},{surname},{date},{city},{email},{phone}")
user(name = input("Введите cвое имя: "), surname = input("Введите свою фамилию: "),date = input("Введите дату рождения: "), city = input("Введите город проживания: "), email = input("Введите свою почту: "), phone = input("Введите номер телефона: "))