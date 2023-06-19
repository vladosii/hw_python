# 8.1[49]. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .csv
# Информация о человеке:
#   Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
#   Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
#   Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
#   Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. 
#   Берем первое совпадение по фамилии.
#   Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
#   Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# Усложнение.
# - Сделать тесты для функций
# - Разделить на model-view-controller

# user=["ferstname","secondname","phone","discription"]
# phone_dir = {1:["ferstname","secondname","phone","discription"],2:["ferstname","secondname","phone","discription"]}


from os.path import join, abspath, dirname, exists

def input_data()->list:
    user = []
    user.append(input("Input ferst name "))
    user.append(input("Input second name "))
    user.append(input("Input phone "))
    user.append(input("Input discription "))
    return user

def create(phone_dir_local: dict, idc: int, user:list) -> tuple:
    idc += 1
    phone_dir_local[idc] = user
    return phone_dir_local, idc

def export_phone_dir(phone_dir: dict, file_name: str):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name+'.txt')
    with open(full_name, mode='w', encoding='utf-8') as file:
        for idc, user in phone_dir.items():
            file.write(f"{idc}#{user[0]}#{user[1]}#{user[2]}#{user[3]}\n")

def search_user(phone_dir_local: dict, searching: str) -> int:
    for idc, user in phone_dir_local.items():
        lastname: str = user[0]
        if lastname.upper().startswith(searching.upper()):
            return idc
    return 0

def print_dict(phone_dir: dict):
    for idc, user in phone_dir.items():
        print(f"{idc}: {user[0]} {user[1]} {user[2]} {user[3]}")

def print_once(phone_dir: dict, id: int):
    user = phone_dir[id]
    print(f"{user[0]} {user[1]} {user[2]} {user[3]}")

def import_phone_dir(phone_dir, file_name):
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, f"{file_name}.txt")
    if not exists(full_name):
        print("Error! File not found.")
        return
    idc = 0
    phone_dir = dict()
    with open(full_name, mode='r', encoding='utf-8') as file:
        for line in file:
            lst = line.strip().split('#')[1:]
            phone_dir, idc = create(phone_dir, idc, lst)
            # print(lst)
    return phone_dir, idc

def delete_user(phone_dir_local: dict, del_index: int)-> bool:
    result = phone_dir_local.pop(del_index, [0])
    if result == 0: 
        print("Not found")
        return False
    print(f"{result} удалено")
    return True

def update_user(phone_dir_local: dict, upd_index: int):
    user = input_data()
    phone_dir_local[upd_index] = user
    print (f'{phone_dir_local[upd_index]} is update')


def menu ():
    print("A-добавить. P-печать. E-экспорт. I-импорт. F-поиск. D-удалить. U-изменить. Q-выход")
    key_count =0
    phone_dir = dict()
    while True:
        user_command = input("Выберите операцию: ").upper()
        if user_command == 'Q':
            break
        elif user_command == "A":
           data = input_data()
           phone_dir, key_count = create(phone_dir, key_count, data)
        elif user_command == 'P':
            print_dict(phone_dir)
        elif user_command == "E":
            file_name = input("Введите имя файла: ")
            export_phone_dir(phone_dir, file_name)
        elif user_command == "I":
            file_name = input("Введите имя файла: ")
            phone_dir, key_count = import_phone_dir(phone_dir, file_name)
            print(f"Импортировано {key_count} записей")
        elif user_command == 'F':
            searching = input("Кого ищем? ")
            idc = search_user(phone_dir, searching)
            if idc == None: print("Not found")
            else: print_once(phone_dir, idc)
        elif user_command == 'D':
            id_delete = int(input("Номер удаляемой записи(0-отмена): "))
            if id_delete != 0:
                delete_user(phone_dir, id_delete)
        elif user_command == 'U':
            data = input("Номер записи или фамилия: ")
            idc = 0
            if data.isdigit():
                idc = int(data)
            else:
                idc = search_user(phone_dir, data)
                if idc == 0:
                    key_count += 1
                    idc = key_count
            update_user(phone_dir, idc)
            


key_count =0
phone_dir = dict()

# user1 = ["Абырвалгов","Гиви","+7(328)123-56-56","discription1"]
# user2 = ["second_name2","first_name2","phone2","discription2"]

# phone_dir, key_count=create(phone_dir,key_count,user1)
# phone_dir, key_count=create(phone_dir,key_count,user2)


# phone_dir = {1: ['Иванов',   'Иван',  '+7(xxx)xxx-xx-xx', 'desription_Иванов'], 
#             2: ['Петров',   'Петр',  '+7(---)xxx-xx-xx', 'desription_Петров'], 
#             3: ['Соколов',  'Илья',  '+7(---)---------', 'desription_Соколов'], 
#             4: ['Павельев', 'Андрей','+7(***)***-**-**', 'desription_Павельев'], 
#             5: ['Пешехов',  'Антон', '+7++++++++++',     'desription_Пешехов'], 
#             6: ['Сааков',   'Илья',  '+7(+++)+++-++-++', 'desription_Сааков'], 
#             }


menu ()
# print_dict(phone_dir)
# print(phone_dir)
# export_phone_dir(phone_dir, "phones")
# print(search_user(phone_dir, "Пеш"))
# phone_dir, key_count = import_phone_dir(phone_dir, 'phones')
# phone_dir, key_count = create(phone_dir, key_count, user1)
# print_dict(phone_dir)
# export_phone_dir(phone_dir, "phones")