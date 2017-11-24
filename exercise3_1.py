# Задание 3 (for)

# Создать список с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.

school_1 = [
            {'school_class': '4a', 'scores': [3,4,4,5,2]}, 
            {'school_class': '4b', 'scores': [5,5,5,3,4]}, 
            {'school_class': '4c', 'scores': [3,3,3,4,4]},
            {'school_class': '3a', 'scores': [5,5,5,4,2]}
            ]

scores_summ = [] # список для сумм оценок по классам
students_class = [] # список для количества учащихся по классам

for scores_t1 in school_1:
       scores_summ.append(sum(scores_t1.get('scores'))) # находим сумму оценок по классам и добавляем в список

for scores_t2 in school_1:
       students_class.append(len(scores_t2.get('scores'))) # находим количество человек в классе и добавляем в список
       
scores_summ_total = sum(scores_summ)
students_class_total = sum(students_class)
avg_scores_shcool1 = scores_summ_total/students_class_total
print('Сумма оценок:',  scores_summ_total)
print('Количество учащихся:', students_class_total)
print('Средний балл по школе', avg_scores_shcool1) # делим сумму оценок на количество человек