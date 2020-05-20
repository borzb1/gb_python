def my_func(a,b,c):
    seq = [a,b,c]
    total = []
    i = 0
    for i in seq:
        i += 1
        maxone = max(seq)
        total.append(maxone)
        seq.remove(maxone)
    print(sum(total))
my_func(220,20,50)
