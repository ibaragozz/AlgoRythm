# mas = [5, 6, 2, 3, 7, 1]
# n = 6
#
# for run in range(n-1):
#     for i in range(n-1-run):
#         if mas[i] > mas[i + 1]:
#             mas[i], mas[i + 1] = mas[i + 1], mas[i]
# print(mas)

# def quick_sort(s):
#
#     if len(s) <= 1:
#         return s
#
#     element = s[0]
#     left = list(filter(lambda i: i < element, s))
#     center = [i for i in s if i == element]
#     right = list(filter(lambda i: i > element, s))
#
#     return quick_sort(left) + center + quick_sort(right)
#
# print(quick_sort([6, 2, 9, 0, 1, 5, 3]))

