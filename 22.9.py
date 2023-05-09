
sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
arbitrary = int(input("Укажите любое число: "))


 # отсортировать полученный список по возрастанию
def establish_order(lst):
    for i in range(len(lst)):
            for j in range(len(lst) - i - 1):
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]


# установить номер позиции элемента, который меньше введенного
# пользователем числа, а следующий за ним больше или равен этому числу
def element_position(lst_sort):
    mid = len(lst_sort) // 2
    low = 0
    high = len(lst_sort) - 1
    while lst_sort[mid] != arbitrary and low <= high:
        if arbitrary > lst_sort[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        print("Указанное вами число отсутствует в введённой последовательности.")
    else:
        print("Указанное вами число занимает позицию между", mid-1, "и",  mid, "элементом")

print("Результат:")
establish_order(sequence)
print("Отсортированный список по возрастанию элементов в нем:", sequence)
element_position(sequence)
