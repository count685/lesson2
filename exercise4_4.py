# Задание 4 (while)

# При помощи функции get_answer() отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

answers = {'привет': 'и тебе привет!', 'как дела': 'лучше всех', 'что нового': 'Ничего особого'}

def get_answer(user_reply):
    return answers.get(user_reply, 'Не понимаю, о чем ты.')

def ask_user():
    user_reply = input('Спроси меня что-нибудь?\n')
    while True:
        if user_reply == 'Пока!':
            print('Повинуюсь!')
            break
        else:
            print(get_answer(user_reply))
            user_reply = input('Спроси меня что-нибудь?\n')

if __name__ == '__main__':
    ask_user()