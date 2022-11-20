def election(*args) -> int:
    return int(sum(args) > len(args) / 2)


line = input().split()
x, y, z = (int(i) for i in line)
print(election(x, y, z))
