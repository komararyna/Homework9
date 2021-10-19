def palin():
    num, n_1, n_2 = 0, 0, 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            multi = i * j
            if str(multi) == str(multi)[::-1] and multi > num:
                n_1, n_2, num = i, j, multi
    print(n_1, '*', n_2, '=', num)
    return
palin()