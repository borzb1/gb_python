seasonslist = ['winter', 'spring', 'summer', 'autumn']
seasonsdict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Введите месяц: "))
if month == 1 or month == 12 or month == 2:
        print(seasonsdict.get(1))
        print(seasonslist[0])
elif month == 3 or month == 4 or month ==5:
    print(seasonsdict.get(2))
    print(seasonslist[1])
elif month == 6 or month == 7 or month == 8:
    print(seasonsdict.get(3))
    print(seasonslist[2])

elif month == 9 or month == 10 or month == 11:
    print(seasonsdict.get(4))
    print(seasonslist[3])
else:
        print("Времени года для такого месяца еще не придумали :)")