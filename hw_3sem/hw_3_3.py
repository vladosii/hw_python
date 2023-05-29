# 3.3[20]: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

## 1 Сбособ, который вообще не эффективен
# list = 'АВЕИНОРСТ'
# list2 = 'ДКЛМПУ'
# list3 = 'БГЁЬЯ'
# list4 = 'ЙЫ'
# list5 = 'ЖЗХЦЧ'
# list6 = 'ШЭЮ'
# list7 = 'ФЩЪ'

# string = 'НОУТБУК'
# sum = 0
# count = 0

# for item in string:
#     for s in list:
#         if (item == s):
#             sum += 1
#     for s in list2:
#         if (item == s):
#             sum += 2
#     for s in list3:
#         if (item == s):
#             sum += 3
#     for s in list4:
#         if (item == s):
#             sum += 4
#     for s in list5:
#         if (item == s):
#             sum += 5
#     for s in list6:
#         if (item == s):
#             sum += 8
#     for s in list7:
#         if (item == s):
#             sum += 10
# print(sum)

# 2 Метод, который я придумал, 
# как мне кажется работает лучше и выглядит красивей
keywords = {
    'А, В, Е, И, Н, О, Р, С, Т': 1,
    'Д, К, Л, М, П, У': 2,
    'Б, Г, Ё, Ь, Я': 3,
    'Й, Ы': 4,
    'Ж, З, Х, Ц, Ч': 5,
    'Ш, Э, Ю': 8,
    'Ф, Щ, Ъ': 10,
    'A, E, I, O, U, L, N, S, T, R':1,
    'D, G':2,
    'B, C, M, P':3,
    'F, H, V, W, Y':4,
    'K':5,
    'J, X':8,
    'Q, Z':10
}

string = 'notebook'
sum = 0

for item in keywords:
    for val in item:
        for let in string:
            if (val == let.upper()):
                sum += keywords[item]

print(sum)