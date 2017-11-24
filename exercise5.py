# Задание 5 (exception)

# Переписать функцию ask_user(), добавив обработку exception-ов
# Добавить перехват ctrl+C и прощание

answers = {'привет': 'и тебе привет!', 'как дела': 'лучше всех', 'что нового': 'Ничего особого'}

def get_answer(question, answers):
    return answers.get(question, 'Не понимаю, о чем ты.')

def ask_user():
    try:
        while True:
            user_input = input('Спроси меня что-нибудь?\n')
            answer = get_answer(user_input, answers)
            print(answer) 

            if user_input == 'Пока!':
                break
            
    except KeyboardInterrupt:
        return print('До свидания! Программа завершена')

if __name__ == '__main__':
    ask_user()