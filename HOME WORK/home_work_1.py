import os
choice_user = 0
my_list = [9, 1, 5, 9, 1]
while choice_user != 5:
    def print_info():
        global choice_user
        print("------------ Работа со списками ------------")
        print("1 - 'ДЕМОНСТРАЦИИ СПИСКА'\n"
              "2 - 'ДОБАВЛЕНИЯ ЭЛЕМЕНТА В КОНЕЦ СПИСКА ИЛИ ПО ИНДЕКСУ'\n"
              "3 - 'УДАЛЕНИЯ ИЗ СПИСКА ПОСЛЕДНЕГО ЭЛЕМЕНТА ИЛИ ЭЛЕМЕНТА ПО ИНДЕКСУ'\n"
              "4 - 'СОРТИРОВКИ СПИСКА'\n"
              "5 - 'ВЫХОД'")
        choice_user = (int(input("Что вы хотите сделать со списком?\n"
                             "'Ведите число': ")))
        if choice_user < 1 or choice_user > 5:
            os.system('cls')
            print("Не корректный ввод")
        elif choice_user == 1:
            if len(my_list) == 0:
                os.system('cls')
                print("Ваш список пуст")

            else:
                os.system('cls')
                print("Ваш список\n",
                      my_list)
        elif choice_user == 2:
            global add_num, num, nun_2, poz
            os.system('cls')
            add_num = (int(input("Куда добавить элемент:\n "
                                      "'1' - в конец списка\n"
                                      " '2' - по индексу\n"
                                      " 'Ведите число': ")))
            if add_num == 1:
                os.system('cls')
                num = (int(input("Какое число добавить:\n ")))
                my_list.append(num)
                print("Новый список:\n",
                      my_list)
            elif add_num == 2:
                os.system('cls')
                print("Размер списка", len(my_list))
                poz = (int(input("На каую позицию добавить новый элемент?\n"
                                   "Индекс: ")))
                nun_2 = (int(input("Какое число добавить?\n"
                                   "Ведите число: ")))
                my_list.insert(poz - 1, nun_2)
                print("Ваш новый список\n",
                      my_list)
        elif choice_user == 3:
            add_num = (int(input("От куда удалить элемент:\n "
                                 "'1' - в конец списка\n"
                                 " '2' - по индексу\n"
                                 " 'Ведите число': ")))
            if add_num == 1:
                os.system('cls')
                my_list.pop()
                print("Новый список", my_list)
            elif add_num == 2 and len(my_list) > 0:
                os.system('cls')
                print(my_list)
                dell_element = (int(input("Какой элемент удалить? 'Ведите индек элемента':")))
                if dell_element < 0 or dell_element > len(my_list):
                    os.system('cls')
                    print("Элемента с таким индексом нет")
                else:
                    os.system('cls')
                    my_list.pop(dell_element - 1)
                    print("Новый список", my_list)
        elif choice_user == 4:
            os.system('cls')
            my_list.sort()
            print("Отсортированный список", my_list)
        elif choice_user == 5:
            os.system('cls')
            print()
            print("Работа со списком закончина пользователем!")
    os.system('cls')
    print_info()

