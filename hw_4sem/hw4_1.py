# Усложнение задач выделены (*). Они необязательны для решения и нужны для тех, кому мало выполнить обычное задание.
# Если вы хотите решить усложненное задание - сначала сделайте задание обычной сложности.

# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах. 
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку

# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

list1 = [2, 4, 6, 8, 10, 10, 8, 6, 4, 2]
list2 = [3, 9, 12, 15, 18]
list3 = ''

for item in list2:
    for val in list1:
        if (item == val):
            list3 += str(item)+' '

if (list3 != ''):
    print(list3)
else:
    print('Нет повторяющихся')