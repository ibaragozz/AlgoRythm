mas = [5, 6, 2, 3, 7, 1]
n = 6

for run in range(n-1):
    for i in range(n-1-run):
        if mas[i] > mas[i + 1]:
            mas[i], mas[i + 1] = mas[i + 1], mas[i]
print(mas)

def quick_sort(s):

    if len(s) <= 1:
        return s

    element = s[0]
    left = list(filter(lambda i: i < element, s))
    center = [i for i in s if i == element]
    right = list(filter(lambda i: i > element, s))

    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([6, 2, 9, 0, 1, 5, 3]))

# CHOSEN SORTING ALGORITHM

a = [5, 6, 2, 3, 7, 1, -6, -9]

def choosen_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

print(choosen_sort(a))

a = [5, 6, 2, 3, 7, 1, -6, -9]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort(a))