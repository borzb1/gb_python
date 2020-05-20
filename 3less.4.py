def my_func(x,y):
    print(x ** y)
my_func(5,-2)

def my_func(x,y):
    res = 1
    for i in range(abs(y)):
        res *= x
    if y >= 0:
        return res
    else:
        return 1/ res
print(my_func(10,-1))


