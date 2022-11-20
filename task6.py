def power(a, n):
    # return a ** n
    s = 1
    for i in range(n):
        s *= a

    return s


line = input().split()
a, n = float(line[0]), int(line[1])

print(power(a, n))
