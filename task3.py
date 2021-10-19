def rec(a, b):
    print(a * '*')
    for i in range(b - 2):
        print('*', '' * (b - 2), '*')
    print(a * '*')
rec(4,5)