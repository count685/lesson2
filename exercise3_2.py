# Задание 3 (for)

# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по каждому классу.

school_1 = [
            {'school_class': '4a', 'scores': [3,4,4,5,2]}, 
            {'school_class': '4b', 'scores': [5,5,5,3,4]}, 
            {'school_class': '4c', 'scores': [3,3,3,4,4]},
            {'school_class': '3a', 'scores': [5,5,5,4,4]}
            ]

for scores_t in school_1:
       print(sum(scores_t.get('scores')) / len(scores_t.get('scores')))
