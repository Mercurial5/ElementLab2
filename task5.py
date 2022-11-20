n = input()

s = 0
power = len(n) - 1
for i in n:
    s += 2 ** power * int(i)
    power -= 1

print(s)
