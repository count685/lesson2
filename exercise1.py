#Задание 1 (if)

# Попросить пользователя ввести возраст.
# По возрасту определить, чем он должен заниматься: учиться в детском саду, школе, ВУЗе или работать.
# Вывести занятие на экран.

age = int(input()) 

if age <= 7:
    print('учится в детском саду')
elif age <= 18:
    print('учтися в школе')
elif age <= 23:
    print('учится в ВУЗе')
elif age >= 24:
    print('работает') 