def x(num):
    if num < 0:
        print('Error')
    if num < 1:
        print(num)
    else:
        x((num - 1) + (num - 2))


n = 3
x(n)

