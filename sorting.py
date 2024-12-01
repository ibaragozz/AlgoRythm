mas = [5, 6, 2, 3, 7, 1]
n = 6

for run in range(n-1):
    for i in range(n-1-run):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)