# Усложнение задач выделены (*). Они необязательны 
# для решения и нужны для тех, кому мало выполнить обычное задание.
# Если вы хотите решить усложненное задание - сначала 
# сделайте задание обычной сложности.

# 3.1[16]: Дан список целых чисел. Требуется вычислить, 
# сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. 
# Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.

list = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]

x = 10

def repeat(x, list):
    count = 0

    condition = count == 0

    for item in list:
        if (x == item):
            count += 1
    if (condition):
        return -1
    return count

result = repeat(x, list)

print(result)