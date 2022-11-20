n = int(input())

for i in range(2, 30001):
    if not n % i:
        print(i)
        break
