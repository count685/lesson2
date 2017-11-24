# Задание 4 (while)

# Написать функцию ask_user() чтобы с помощью input() спрашивать пользователя “Как дела?”, пока он не ответит “Хорошо”

def ask_user():
    user_reply = input('Как дела?\n')
    while True:
        if user_reply == 'Хорошо':
            print('Ну и чудненько!')
            break
        else:
            user_reply = input('Как дела?\n')

if __name__ == '__main__':
    ask_user()
