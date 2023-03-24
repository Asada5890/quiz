#Вопрос ответ
tasks = [
    ("Столица России?", "МОСКВА"), 
    ("Столица Франции?", "ПАРИЖ"), 
    ("Столица Германии?", "БЕРЛИН")
]


for task in tasks:
    question, right_answer = task

    users_answer = input(f"{question}\n").upper()

    if users_answer == right_answer:
        print("Все верно!")
    else:
        print("Не верно!")