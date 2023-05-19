# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

data = 653

def summary(data):
    num = data//100
    num1 = data//10%10
    num2 = data%10
    sum = num+num1+num2
    print('Сумма чисел: '+str(num)+'+'+str(num2)+'+'+str(num1)+'='+str(sum))

summary(data)