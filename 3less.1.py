def my_f(a, b):
    print(a / b)
try:
    my_f(int(input("Введите делимое: ")), int(input("Введите делитель: ")))
except ZeroDivisionError:
    print("На ноль делить нельзя!")

