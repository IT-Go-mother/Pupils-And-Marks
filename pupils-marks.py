logins = {
    'Erik' : 12,
    'Anton' : 8,
    'Oleh' : 9
}
def Create_Pupil():
    create_login = input('\nВведіть ім`я нового учня -> ')
    create_mark = int(input(f'\nВведіть оцінку учня {create_login} -> '))
    logins[create_login] = create_mark
def Read_Pupils():
    for i, j in logins.items():
        print(f'\nІм`я - {i}\nОцінка - {j}\n')
def Update_Pupil():
    x=0
    what_update = input('\nВведіть ім`я, яке Ви хочете змінити -> ')
    for i in logins.keys():
        if i == what_update:
            x+=1
    if x>0:
        new_mark = input(f'\nДобре, введіть нову оцінку для школяра {what_update} -> ')
        logins[what_update] = new_mark
    else:
        print("\nПомилка, такого ім'я не має у списку. Спробуйте ще!")
def Delete_Pupil():
    what_delete = input("Введіть ім'я, яке Ви хочете видалити -> ")
    x=0
    for i in logins.keys():
        if i == what_delete:
            x+=1
    if x>0:
        del logins[what_delete]
    else:
        print("\nПомилка, такого ім'я не має у списку. Спробуйте ще!")
def Work():
    while True:
        operation = int(input("\nДоброго дня! Вас вітає список учнів та їхніх оцінок.\n[1] - Створити нового учня\n[2] - Вивести список усіх учнів та їхніх оцінок\n[3] - Змінити оцінку у учня\n[4] - Вилучити учня зі списку\n[0] - Завершити програму.\nВведіть операцію -> "))
        if operation == 1:
            Create_Pupil()
        elif operation == 2:
            Read_Pupils()
        elif operation == 3:
            Update_Pupil()
        elif operation == 4:
            Delete_Pupil()
        elif operation == 0:
            print('До побачення!')
            break
Work()
