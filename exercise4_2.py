# Задание 4 (while)

# Предыдущие задание:

# Пройдите в цикле по списку ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"] пока не встретите имя "Валера". 
# Когда найдете напишите "Валера нашелся". Подсказка: используйте метод list.pop()

# Текущее задание:

# Перепишите предыдущий пример в виде функции find_person(name), которая ищет имя в списке.

user_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]

def find_person(name):
    while True:
        if name == user_list.pop(0):
            print('нашел')
            break

find_person('Валера') 
find_person('Антон') # Функция возвращает ошибку, так как при проверке списка 
                    # из списка последовательно удаляются элементы и в итоге остается пустой список
