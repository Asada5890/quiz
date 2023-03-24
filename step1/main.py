#Вопрос ответ

task = ("Столица России?", "МОСКВА")

question, right_answer = task

users_answer = input(f"{question}\n").upper()

if users_answer == right_answer:
    print("Все верно!")
else:
    print("Не верно!")