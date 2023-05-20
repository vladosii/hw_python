# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).


def chocolate(n, m , k):
    
    stateOne = k < n * m
    stateTwo = k % n == 0 or k % m == 0
    
    # print(stateOne)
    # print(stateTwo)

    if stateOne and stateTwo:
        return 'Yes'
    else:
        return 'No'

result = chocolate(3, 2, 4)

print(result)