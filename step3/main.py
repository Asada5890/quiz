#Вопрос ответ
tasks = [
    ("Столица России?", "МОСКВА", 2), 
    ("Столица Франции?", "ПАРИЖ", 3), 
    ("Столица Германии?", "БЕРЛИН", 3)
]

points = 0

for task in tasks:
    question, right_answer, point = task

    users_answer = input(f"{question}\n").upper()

    if users_answer == right_answer:
        print("Все верно!")
        points += point
    else:
        print("Не верно!")

print("Вы набрали баллов:", points)