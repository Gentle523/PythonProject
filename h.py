n = int(input("Введіть число n: "))
if n % 2 != 0:
    n = n - 1
for i in range(n, 1, -2):
    print(i, end=" ")