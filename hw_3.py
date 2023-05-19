# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

def ticket(number):
    strNumber = str(number)
    length = len(strNumber)
    i = 0
    sum = 0
    for item in strNumber:
        if (i < 3):
            sum = sum + int(item)
            i = i + 1
    # print(sum)

    sum2 = 0
    max = length-3
    for item in strNumber:
        if (max != length):
            sum2 = sum2 + int(strNumber[max])
            max = max+1
    # print(sum2)
    
    result = sum == sum2

    if result:
        print('Счастливый билет')
    else:
        print('Не счастливый билет')

    # print(number)

ticket(123412)