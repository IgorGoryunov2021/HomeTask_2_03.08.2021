# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().


count = int(input('Введите желаемое количество цифр'))

i = count
my_list = []
a = my_list

while i > 0:
    digit = input("Введите число" .format(i))
    my_list.append(digit)
    i -= 1
    print(my_list)


j = 0
for i in range(int(len(a) / (2))):
        a[j], a[j + 1] = a[j + 1], a[j]
        j += 2
        print(my_list)




