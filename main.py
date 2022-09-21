def Close10(x, y):

    if abs(10-x) < abs(10-y):
        return x

    elif abs(10-x) > abs(10-y):
        return y

    else:
        return 0

print(Close10(9,15))